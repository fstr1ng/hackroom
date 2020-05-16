from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, permissions

from .serializers import CategorySerializer, PolicySerializer, SignatureSerializer
from .models import Category, Policy, File, Signature

class IndexPage(View):
    def get(self, request):
        context = {
            'num_of_categories': Category.objects.count(),
            'num_of_policies': Policy.objects.count(),
            'num_of_files': File.objects.count(),
            'latest_policies_list': Policy.objects.order_by('-updated_ts')[:5] 
        }
        return render(request, 'hackroom/index.html', context)

class CategoryList(ListView):
    model = Category

class CategoryCreate(CreateView):
    model = Category
    fields = ['name', 'description']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        print(context)
        return context
    def get_success_url(self):
        return reverse('hackroom:category_list')

class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name', 'description']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context
    def get_success_url(self):
        return reverse('hackroom:category_list')

class PolicyList(ListView):
    model = Policy

class PolicyCreate(CreateView):
    model = Policy
    fields = ['name', 'issue', 'type', 'categories', 'description', 'example', 'signature', 'active']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        print(context)
        return context
    def get_success_url(self):
        return reverse('hackroom:policy_list')

class PolicyUpdate(UpdateView):
    model = Policy
    fields = ['name', 'issue', 'type', 'categories', 'description', 'example', 'signature', 'active']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context
    def get_success_url(self):
        return reverse('hackroom:policy_list')

class PolicyDetail(DetailView):
    model = Policy

class FileList(ListView):
    model = File

class SignatureList(ListView):
    model = Signature

class SignatureCreate(CreateView):
    model = Signature
    fields = ['options', 'logic']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        print(context)
        return context
    def get_success_url(self):
        return reverse('hackroom:signature_list')

class SignatureUpdate(UpdateView):
    model = Signature
    fields = ['options', 'logic']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context
    def get_success_url(self):
        return reverse('hackroom:signature_list')

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    permission_classes = [permissions.IsAuthenticated]

class SignatureViewSet(viewsets.ModelViewSet):
    queryset = Signature.objects.all()
    serializer_class = SignatureSerializer
    permission_classes = [permissions.IsAuthenticated]
