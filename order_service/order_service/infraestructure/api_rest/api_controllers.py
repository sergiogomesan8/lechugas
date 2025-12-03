from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from order_service.application.use_cases.create_order.create_order import CreateOrder
from order_service.application.use_cases.create_order.dtos import CreateOrderDTO


from order_service.infraestructure.database.postgresql.persistence.order_persistence import OrderPersistence
from order_service.infraestructure.events.rabbitmq.rabbitmq_event_publisher import RabbitMQEventPublisher
from order_service.infraestructure.events.rabbitmq.rabbitmq_connection import RabbitMQConnection

from order_service.infraestructure.api_rest.api_serializers import CreateOrderSerializer

# Instancias de repositorio y publisher (inyección simple)
rabbitmq_connection = RabbitMQConnection()
publisher = RabbitMQEventPublisher(rabbitmq_connection)

repository = OrderPersistence()
create_order_usecase = CreateOrder(repository, publisher)

class CreateOrderView(APIView):
    def post(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_order_dto = CreateOrderDTO(items=serializer.validated_data['items'])

        order = create_order_usecase.create_order(create_order_dto)
        return Response({"order_id": str(order.id), "status": order.status.value}, status=status.HTTP_201_CREATED)
