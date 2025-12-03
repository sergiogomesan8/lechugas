from order_service.infraestructure.events.rabbitmq.rabbitmq_connection import RabbitMQConnection
from order_service.infraestructure.events.rabbitmq.config import RABBITMQ_EXCHANGE, RABBITMQ_QUEUE
from order_service.application.events.event_bus import EventBus
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

class RabbitMQListener:
    def __init__(self, rabbit_connection: RabbitMQConnection, event_bus: EventBus):
        logging.info("RabbitMQListener → __init__ ejecutado")
        self.event_bus = event_bus
        self.channel = rabbit_connection.get_channel()
        self.queue_name = RABBITMQ_QUEUE

        self.channel.queue_declare(queue=self.queue_name)
        self.channel.queue_bind(exchange=RABBITMQ_EXCHANGE, queue=self.queue_name)
        logging.info("RabbitMQListener → Conexión y bindings configurados")

    def _callback(self, ch, method, properties, body):
        logging.info(f"✅ [RabbitMQListener] Evento recibido: {body}")
        self.event_bus.dispatch(body)

    def start(self):
        logging.info("✅ [RabbitMQListener] Iniciando consumo de eventos...")
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self._callback,
            auto_ack=True
        )
        self.channel.start_consuming()
