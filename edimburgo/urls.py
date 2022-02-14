from django.urls import path, include
from rest_framework.routers import DefaultRouter

from edimburgo import views

# router = DefaultRouter()
# router.register('edimburgo', views.EdimburgoViewSet)
#
# app_name = 'edimburgo'

urlpatterns = [
    #path('', include(router.urls)),
    path('edimburgo/', views.DatosListsView_Edimburgo.as_view(), name='crear_edimburgo'),
    path('edimburgo/<int:pk>/', views.DatosDetailView_Edimburgo.as_view(), name='datos_edimburgo-detail'),
]