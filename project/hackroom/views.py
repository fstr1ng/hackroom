from django.views.generic import ListView
from django.views.generic.base import TemplateView

from rest_framework import viewsets, permissions

from hackroom import serializers, models

class CategoryListView(TemplateView):
    template_name = 'hackroom/category_list.html'

class IndexView(TemplateView):
    template_name = 'hackscan/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Clamav database manager'
        return context


### API Viewsets ###

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
#   permission_classes = [permissions.IsAuthenticated]

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = models.Policy.objects.all()
    serializer_class = serializers.PolicySerializer
#   permission_classes = [permissions.IsAuthenticated]

class FileViewSet(viewsets.ModelViewSet):
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer
#   permission_classes = [permissions.IsAuthenticated]

class SignatureViewSet(viewsets.ModelViewSet):
    queryset = models.Signature.objects.all()
    serializer_class = serializers.SignatureSerializer
#   permission_classes = [permissions.IsAuthenticated]

class SubSignViewSet(viewsets.ModelViewSet):
    queryset = models.SubSign.objects.all()
    serializer_class = serializers.SubSignSerializer
#   permission_classes = [permissions.IsAuthenticated]

class OptionViewSet(viewsets.ModelViewSet):
    queryset = models.Option.objects.all()
    serializer_class = serializers.OptionSerializer
#   permission_classes = [permissions.IsAuthenticated]
