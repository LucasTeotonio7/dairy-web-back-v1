from django.urls import path, include

from rest_framework import routers

from apps.product.api.views.general_views import MeasureUnitView, CategoryView, BrandView
from apps.product.api.views.product_views import ProductView
from apps.product.api.views.price_views import PriceView, PriceProductSupplierView
from apps.product.api.views.supplier_payment_view import SupplierPaymentView
from apps.product.api.views.weekly_control_event_views import WeeklyControlEventView
from apps.product.api.views.weekly_control_views import WeeklyControlView
from apps.product.api.views.purchase_views import PurchaseView


router = routers.DefaultRouter()
router.register(r'measure-unit', MeasureUnitView, basename='measure_unit')
router.register(r'category', CategoryView, basename='category')
router.register(r'brand', BrandView, basename='brand')
router.register(r'product', ProductView, basename='product')
router.register(r'price', PriceView, basename='price')
router.register(r'price-product-supplier', PriceProductSupplierView, basename='price_product_supplier')
router.register(r'weekly-control', WeeklyControlView, basename='weekly_control')
router.register(r'weekly-control-event', WeeklyControlEventView, basename='weekly_control_event')
router.register(r'purchase', PurchaseView, basename='purchase')
router.register(r'supplier-payment', SupplierPaymentView, basename='supplier_payment')

urlpatterns = [
    path('', include(router.urls)),
]
