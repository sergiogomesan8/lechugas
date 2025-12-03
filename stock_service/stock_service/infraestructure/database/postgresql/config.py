from stock_service.settings.config import BASE_DIR
import os

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("STOCK_DB_NAME"),
        'USER': os.getenv("STOCK_DB_USER"),
        'PASSWORD': os.getenv("STOCK_DB_PASSWORD"),
        'HOST': os.getenv("STOCK_DB_HOST"),
        'PORT': os.getenv("STOCK_DB_PORT"),
    }
}