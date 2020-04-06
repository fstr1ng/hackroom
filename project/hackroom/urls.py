from django.urls import path
from . import views

app_name = 'hackroom'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:policy_id>', views.detail, name='detail'),
]
