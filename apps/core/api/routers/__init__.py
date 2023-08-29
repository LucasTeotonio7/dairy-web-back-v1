from django.urls import path, include

from rest_framework import routers

from apps.core.api.views.supplier_views import SupplierView


router = routers.DefaultRouter()
router.register(r'supplier', SupplierView, basename='supplier')

urlpatterns = [
    path('', include(router.urls)),
]
