from django.urls import path, include

from rest_framework import routers

from apps.core.api.views.supplier_views import SupplierView
from apps.core.api.views.user_views import UserView


router = routers.DefaultRouter()
router.register(r'supplier', SupplierView, basename='supplier')
router.register(r'user', UserView, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
