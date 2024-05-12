from . import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include("accounts.urls")),
    path('api/v1/', include('comments.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls"))
    ]