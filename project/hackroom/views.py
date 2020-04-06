from django.views import View
from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Category, Policy
from .forms import PolicyForm

class IndexPage(View):
    def get(self, request):
        context = {
            'amount_of_categories': Category.objects.count(),
            'latest_policies_list': Policy.objects.order_by('-updated_ts')[:5] 
        }
        return render(request, 'hackroom/index.html', context)

class CategoriesList(ListView):
    model = Category
    context_object_name = 'categories_list'

def policy_show(request, policy_id):
    policy = get_object_or_404(Policy, pk=policy_id)
    return render(request, 'hackroom/detail.html', {'policy': policy})

def policy_add(request):
    form = PolicyForm()
    return render(request, 'hackroom/create.html', {'form': form})
