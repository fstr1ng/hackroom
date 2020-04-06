from django.urls import path
from . import views

app_name = 'hackroom'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('category/', views.CategoriesList.as_view()),
    path('policy/add/', views.policy_add, name='policy_add'),
    path('policy/show/<int:policy_id>', views.policy_show, name='policy_show'),
]
