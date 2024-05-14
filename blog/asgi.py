import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

import django
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()

from comments.routing import websocket_urlpatterns

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
            URLRouter(
                websocket_urlpatterns
            )
        ),
})
