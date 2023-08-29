from django.urls import path, include

from rest_framework import routers

from apps.product.api.views.general_views import MeasureUnitView


router = routers.DefaultRouter()
router.register(r'measure_unit', MeasureUnitView, basename='measure_unit')

urlpatterns = [
    path('', include(router.urls)),
]
