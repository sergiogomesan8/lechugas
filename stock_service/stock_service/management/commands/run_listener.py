import time
import logging
import pika

from django.core.management.base import BaseCommand

from stock_service.infraestructure.events.rabbitmq.rabbitmq_event_listener import RabbitMQListener
from stock_service.infraestructure.events.rabbitmq.rabbitmq_connection import RabbitMQConnection

from stock_service.application.events.event_bus import EventBus
from stock_service.application.events.event_handlers.handle_order_created import OrderCreatedEventHandler
from stock_service.application.events.event_handlers.handle_restock_product import ProductStockedBySupplier

from stock_service.infraestructure.database.postgresql.persistence.product_persistence import ProductPersistence
from stock_service.application.use_cases.reduce_stock_for_product.reduce_stock_for_product import ReduceProductStock

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

event_bus = EventBus()

#order.created context event
repository = ProductPersistence()
reduce_product_stock_use_case = ReduceProductStock(repository)
event_bus.register_handler("order.created", OrderCreatedEventHandler(reduce_product_stock_use_case))

class Command(BaseCommand):
    help = "Inicia el listener de RabbitMQ para procesar eventos"

    def handle(self, *args, **kwargs):
        rabbitmq_connection = RabbitMQConnection()
        listener = RabbitMQListener(rabbitmq_connection, event_bus)

        logging.info("Iniciando listener de RabbitMQ...")

        while True:
            try:
                listener.start()
            except pika.exceptions.AMQPConnectionError as e:
                logging.warning(f"RabbitMQ no disponible: {e}. Reintentando en 3s...")
                time.sleep(3)
            except KeyboardInterrupt:
                logging.info("Listener detenido manualmente")
                break
            except Exception as e:
                logging.error(f"Error en listener.start(): {e}")
                time.sleep(3)
