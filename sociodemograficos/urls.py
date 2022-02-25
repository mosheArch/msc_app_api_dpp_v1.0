from django.urls import path, include
from rest_framework.routers import DefaultRouter

from sociodemograficos import views

# router = DefaultRouter()
#router.register('sociodemograficos', views.DatosSociodemograficosViewSet)
#router.register('crear', views.CrearDatosViewSet)

#app_name = 'sociodemograficos'

urlpatterns = [
    path('sociodemograficos/', views.DatosListsView_Sociodemograficos.as_view({'get': 'list'}), name='crear_datos'),
    path('sociodemograficos/<int:pk>/', views.DatosDetailView_Sociodemograficos.as_view(), name='datos-detail'),
]