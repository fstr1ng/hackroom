from django.urls import include, path
from rest_framework import routers
from hackroom import views

router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('policy', views.PolicyViewSet)
router.register('file', views.FileViewSet)
router.register('signature', views.SignatureViewSet)
router.register('subsign', views.SubSignViewSet)
router.register('option', views.OptionViewSet)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framefork')),
    path('category/', views.CategoryListView.as_view(), name='category_list'),
]
