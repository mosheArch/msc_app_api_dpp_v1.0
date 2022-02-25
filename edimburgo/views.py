from rest_framework import viewsets, mixins, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models.model_edimburgo import CuestionarioEdimburgo
from edimburgo import serializers


# class EdimburgoViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     queryset = CuestionarioEdimburgo.objects.all()
#     serializer_class = serializers.datos_cuestionarioEdimburgo_serializer
#
#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user).order_by('user_id')
#
#
# # class CrearCuestionarioViewSet(EdimburgoViewSet):
# #     """Manage tags in the database"""
# #     queryset = CuestionarioEdimburgo.objects.all()
# #     serializer_class = serializers.datos_cuestionarioEdimburgo_serializer

# class DatosListsView_Edimburgo(APIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         datos = CuestionarioEdimburgo.objects.all()
#         serializer = serializers.datos_cuestionarioEdimburgo_serializer(datos, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = serializers.datos_cuestionarioEdimburgo_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DatosListsView_Edimburgo(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = CuestionarioEdimburgo.objects.all()
    serializer_class = serializers.datos_cuestionarioEdimburgo_serializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('user_id')

    def post(self, request):
        serializer = serializers.datos_cuestionarioEdimburgo_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DatosDetailView_Edimburgo(generics.RetrieveAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = CuestionarioEdimburgo.objects.all()
    serializer_class = serializers.datos_cuestionarioEdimburgo_serializer
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('user_id')

    def put(self, request, pk):
        try:
            datos = CuestionarioEdimburgo.objects.get(pk=pk)
        except CuestionarioEdimburgo.DoesNotExist:
            return Response({'Error': 'Este cuestionario no existe'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.datos_cuestionarioEdimburgo_serializer(datos, data=request.data)
        if serializer.is_valid() and self.queryset.filter(user=self.request.user).order_by('user_id'):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            datos = CuestionarioEdimburgo.objects.get(pk=pk)
        except CuestionarioEdimburgo.DoesNotExist:
            return Response({'Error': 'El cuestionario no existe'}, status=status.HTTP_404_NOT_FOUND)

        datos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)