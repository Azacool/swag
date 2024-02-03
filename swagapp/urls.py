from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', GetMethod, basename='product')
router.register('category', CategoryOption, basename='category')
router.register('customers', Customer, basename='customer')
router.register('purchases', Purchase, basename='purchase')
router.register(r'purchases/(?P<customer_id>\d+)/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', Purchase, basename='purchase')

urlpatterns = router.urls

