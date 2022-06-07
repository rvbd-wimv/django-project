from django.shortcuts import render

from rest_framework import viewsets
from django.contrib.auth.models import User

from m_api.serializers import UserSerializer, CustomerSerializer, CustomerTypeSerializer
from m_api.models import Customer, CustomerType

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer

class CustomerViewSet(viewsets.ModelViewSet):
   queryset = Customer.objects.all()
   serializer_class = CustomerSerializer

class CustomerTypeViewSet(viewsets.ModelViewSet):
   queryset = CustomerType.objects.all()
   serializer_class = CustomerTypeSerializer