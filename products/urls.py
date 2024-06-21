from django.urls import path, include
from rest_framework import routers
from .views import ProductView

router = routers.DefaultRouter()
router.register(r'products', ProductView, 'products')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
