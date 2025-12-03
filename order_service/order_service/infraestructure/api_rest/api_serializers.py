from rest_framework import serializers
from order_service.domain.value_objects.order_item import OrderItem
from order_service.application.use_cases.create_order.dtos import CreateOrderDTO

class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.CharField()
    quantity = serializers.IntegerField(min_value=1)

    def to_internal_value(self, data):
        validated_data = super().to_internal_value(data)
        return OrderItem(
            product_id=validated_data['product_id'],
            quantity=validated_data['quantity']
        )

class CreateOrderSerializer(serializers.Serializer):
    items = OrderItemSerializer(many=True)

    def create_order_dto(self) -> CreateOrderDTO:
        items = [OrderItem(**item) for item in self.validated_data['items']]
        return CreateOrderDTO(items=items)