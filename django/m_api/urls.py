'''
from django.urls import include, path

from rest_framework import routers

from m_api.views import UserViewSet, CustomerViewSet, CustomerTypeViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'customertype', CustomerTypeViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
'''