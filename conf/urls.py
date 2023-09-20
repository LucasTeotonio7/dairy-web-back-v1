from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('docs.routers')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/', include('apps.core.api.routers')),
    path('api/', include('apps.product.api.routers')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
