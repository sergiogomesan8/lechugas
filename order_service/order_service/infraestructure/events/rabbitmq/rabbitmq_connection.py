import pika
from order_service.infraestructure.events.rabbitmq.config import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USER, RABBITMQ_PASSWORD, RABBITMQ_EXCHANGE, RABBITMQ_QUEUE
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class RabbitMQConnection:
    def __init__(self):
        logging.info("RabbitMQConnection - Realizando la conexión...")
        try:
            credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
            params = pika.ConnectionParameters(
                host=RABBITMQ_HOST, 
                port=RABBITMQ_PORT, 
                credentials=credentials
            )
            self.connection = pika.BlockingConnection(params)
            self.channel = self.connection.channel()
            self.channel.exchange_declare(exchange=RABBITMQ_EXCHANGE, exchange_type='fanout')
        except Exception as e:
            logging.info(f"RabbitMQConnection → Error conectando a RabbitMQ: {e}")
            raise
    def get_channel(self):
        return self.channel