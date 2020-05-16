from django.contrib.auth.models import User, Group
from rest_framework import serializers

from hackroom.models import Category, Policy, File, Signature, SubSign, Option

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'id', 'name', 'description']

class PolicySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Policy
        fields = ['url', 'id', 'issue', 'type', 'name', 'categories', 'description', 'example', 'file_set', 'signature', 'created_ts', 'updated_ts', 'active']

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ['url', 'id']

class SignatureSerializer(serializers.ModelSerializer):
    def display_value(self, instance):
        return str(instance)
    class Meta:
        model = Signature
        fields = ['url', 'id', 'options', 'subsigns', 'logic']

class SubSignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubSign
        fields = ['url', 'id', 'type', 'value']

class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = ['url', 'id', 'key', 'value']
