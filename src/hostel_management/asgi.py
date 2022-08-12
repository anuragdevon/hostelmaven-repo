import os

from django.core.asgi import get_asgi_application

ServiceModule = os.getenv('SERVICE_MODULE')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", ServiceModule)

application = get_asgi_application()
