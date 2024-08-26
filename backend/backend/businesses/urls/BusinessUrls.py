from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views import BusinessViewSet
router = DefaultRouter()
router.register(r'businesses',BusinessViewSet,basename='businesses')

urlpatterns = [
    path('',include(router.urls)),
]
