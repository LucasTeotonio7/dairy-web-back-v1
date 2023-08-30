from django.urls import path, include

from rest_framework import routers

from apps.product.api.views.general_views import MeasureUnitView, CategoryView, BrandView
from apps.product.api.views.product_views import ProductView


router = routers.DefaultRouter()
router.register(r'measure_unit', MeasureUnitView, basename='measure_unit')
router.register(r'category', CategoryView, basename='category')
router.register(r'brand', BrandView, basename='brand')
router.register(r'product', ProductView, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
