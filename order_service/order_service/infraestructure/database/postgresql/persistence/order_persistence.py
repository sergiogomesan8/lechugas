from order_service.domain.ports.order_repository import IOrderRepository
from order_service.domain.entities.order import Order

from order_service.infraestructure.database.postgresql.models.order_model import OrderModel
from order_service.infraestructure.database.postgresql.models.order_item_model import OrderItemModel


class OrderPersistence(IOrderRepository):

    def create_order(self, order: Order) -> None:
        print(f"OrderPersitence -> create_order - order: {order}")

        order_model = OrderModel.objects.create(
            id=str(order.id),
            order_date=order.order_date.value,
            status=order.status
        )

        for item in order.items:
            OrderItemModel.objects.create(
                order=order_model,
                product_id=item.product_id,
                quantity=item.quantity
            )