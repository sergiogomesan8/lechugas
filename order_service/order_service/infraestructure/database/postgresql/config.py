from order_service.settings.config import BASE_DIR
import os

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("ORDER_DB_NAME"),
        'USER': os.getenv("ORDER_DB_USER"),
        'PASSWORD': os.getenv("ORDER_DB_PASSWORD"),
        'HOST': os.getenv("ORDER_DB_HOST"),
        'PORT': os.getenv("ORDER_DB_PORT"),
    }
}