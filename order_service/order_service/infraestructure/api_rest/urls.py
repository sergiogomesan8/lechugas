from django.urls import path

from order_service.infraestructure.api_rest.api_controllers import CreateOrderView

urlpatterns = [
    path('orders/', CreateOrderView.as_view(), name='create-order'),
]