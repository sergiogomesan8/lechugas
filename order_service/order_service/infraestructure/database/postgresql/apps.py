from django.apps import AppConfig

class PostgresqlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order_service.infraestructure.database.postgresql'