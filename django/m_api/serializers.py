from rest_framework import serializers
from django.contrib.auth.models import User, Group
from m_api.models import Customer, CustomerType


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('name')


class CustomerSerializer(serializers.ModelSerializer):

   class Meta:
       model = Customer
       fields = ('name', 'address', 'city', 'postalcode', 'contact_name', 'contact_phone','email','customer_type')


class CustomerTypeSerializer(serializers.ModelSerializer):
   class Meta:
       model = CustomerType
       fields = ('type_name',)

