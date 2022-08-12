import os
from django.core.wsgi import get_wsgi_application


import os

from django.core.wsgi import get_wsgi_application

ServiceModule = os.getenv('SERVICE_MODULE')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", ServiceModule)

application = get_wsgi_application()
