import json 
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class EventBus:
    def __init__(self):
        self._handlers = {}

    def register_handler(self, event_name: str, handler):
        if event_name not in self._handlers:
            self._handlers[event_name] = []
        self._handlers[event_name].append(handler)
        logging.info(f"Handler registrado para: {event_name}")

    def dispatch(self, raw_body: bytes):
        try:
            data = json.loads(raw_body)
            logging.info(f"Data: {data}")
        except Exception:
            logging.info("❌ Error: el mensaje recibido no es JSON válido:", raw_body)
            return

        event_name = data.get("event_name")
        payload = data.get("payload")

        if not event_name:
            logging.info("❌ Error: el mensaje no contiene 'event_name'")
            logging.info("Mensaje recibido:", data)
            return

        for handler in self._handlers[event_name]:
            try:
                handler.handle(payload)
            except Exception as e:
                logging.warning(f"⚠️ No handler registrado para {event_name}")