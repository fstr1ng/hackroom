from django.contrib.auth.models import User, Group
from rest_framework import serializers

from hackroom.models import Category, Policy, Signature

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'name', 'description']

class PolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Policy
        fields = ['url', 'id', 'issue', 'type', 'name', 'categories', 'description', 'example', 'signature', 'active']

class SignatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Signature
        fields = ['url', 'id', 'options', 'subsigns', 'logic']
