from m_api.views import UserViewSet, CustomerViewSet, CustomerTypeViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'users',UserViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'customertype', CustomerTypeViewSet)

