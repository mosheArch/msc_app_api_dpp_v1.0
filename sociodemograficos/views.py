from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models.model_datosSociodemograficos import DatosSociodemograficos
from sociodemograficos import serializers


# class DatosSociodemograficosViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     queryset = DatosSociodemograficos.objects.all()
#     serializer_class = serializers.datos_sociodemograficos_serializer
#
#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user).order_by('user_id')


# class CrearDatosViewSet(DatosSociodemograficosViewSet):
#     """Manage tags in the database"""
#     queryset = DatosSociodemograficos.objects.all()
#     serializer_class = serializers.datos_sociodemograficos_serializer


class DatosListsView_Sociodemograficos(APIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        datos = DatosSociodemograficos.objects.all()
        serializer = serializers.datos_sociodemograficos_serializer(datos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.datos_sociodemograficos_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DatosDetailView_Sociodemograficos(APIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            datos = DatosSociodemograficos.objects.get(pk=pk)
        except DatosSociodemograficos.DoesNotExist:
            return Response({'Error': 'El dato no existe'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.datos_sociodemograficos_serializer(datos)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            datos = DatosSociodemograficos.objects.get(pk=pk)
        except DatosSociodemograficos.DoesNotExist:
            return Response({'Error': 'El dato no existe'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.datos_sociodemograficos_serializer(datos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            datos = DatosSociodemograficos.objects.get(pk=pk)
        except DatosSociodemograficos.DoesNotExist:
            return Response({'Error': 'El dato no existe'}, status=status.HTTP_404_NOT_FOUND)

        datos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
