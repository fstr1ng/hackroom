from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'hackroom'

router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('policy', views.PolicyViewSet)
router.register('signature', views.SignatureViewSet)

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('category/', views.CategoryList.as_view(), name='category_list'),
    path('category/add/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/update/<int:pk>/', views.CategoryUpdate.as_view(), name='category_update'),

    path('policy/', views.PolicyList.as_view(), name='policy_list'),
    path('policy/add/', views.PolicyCreate.as_view(), name='policy_create'),
    path('policy/update/<int:pk>/', views.PolicyUpdate.as_view(), name='policy_update'),
    path('policy/<int:pk>/', views.PolicyDetail.as_view(), name='policy_detail'),

    path('file/', views.FileList.as_view(), name='file_list'),

    path('signature/', views.SignatureList.as_view(), name='signature_list'),
    path('signature/add', views.SignatureCreate.as_view(), name='signature_create'),
    path('signature/update', views.SignatureUpdate.as_view(), name='signature_update'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framefork')),
    path('api/', include(router.urls)),
]
