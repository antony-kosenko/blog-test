from . import settings
from django.contrib import admin
from django.urls import path, include

from comments.views import test_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test_view, name='ws_test'),
    path('api/v1/accounts/', include("accounts.urls")),
    path('api/v1/', include('comments.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls"))
    ]
