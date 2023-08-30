from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('docs.routers')),
    path('api/', include('apps.core.api.routers')),
    path('api/', include('apps.product.api.routers')),
]
