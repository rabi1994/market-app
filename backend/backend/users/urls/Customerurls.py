from rest_framework.routers import DefaultRouter
from django.urls import path, include
from ..views.CustomerViewSet import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')

urlpatterns = [
    path('', include(router.urls)),
]