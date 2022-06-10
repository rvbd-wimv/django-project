from django.shortcuts import render

from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group

from m_api.serializers import UserSerializer, GroupSerializer, CustomerSerializer, CustomerTypeSerializer
from m_api.models import Customer, CustomerType


from oauth2_provider.contrib.rest_framework import TokenHasScope
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [TokenHasScope]
    required_scopes = ['users']
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [TokenHasScope]
    required_scopes = ['customers']
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [TokenHasScope]
    required_scopes = ['customers']
    queryset = CustomerType.objects.all()
    serializer_class = CustomerTypeSerializer
