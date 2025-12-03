import json
from order_service.domain.ports.event_publisher_interface import IEventPublisher
from order_service.infraestructure.events.rabbitmq.rabbitmq_connection import RabbitMQConnection
from order_service.infraestructure.events.rabbitmq.config import RABBITMQ_EXCHANGE, RABBITMQ_QUEUE


class RabbitMQEventPublisher(IEventPublisher):
    def __init__(self, rabbit_connection: RabbitMQConnection):
        self.channel = rabbit_connection.get_channel()

    def publish(self, event):
        body = json.dumps({
            "event_name": event.name,
            "payload": event.payload
        })
        self.channel.basic_publish(
            exchange=RABBITMQ_EXCHANGE,
            routing_key=RABBITMQ_QUEUE,
            body=body
        )
