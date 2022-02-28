from rest_framework import viewsets, mixins, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models.model_edimburgo import CuestionarioEdimburgo, resultdoEdimburgo
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
            id_user = serializer.data.get('user')
            cuestionario = serializer.data.values()
            cuestionario = list(cuestionario)
            del cuestionario [0]
            del cuestionario [-1]
            suma = sum(cuestionario[:-1])

            if cuestionario[-2] > 0:
                guardar = resultdoEdimburgo(resultado=suma,
                                            comentarios="Cualquier puntaje distinto de cero en la pregunta N° 10 requiere de evaluación adicional dentro de 24 horas.",
                                            user_id=id_user)
                guardar.save()
            elif (suma>= 13 and cuestionario[-1] =='Embarazo'):
                guardar = resultdoEdimburgo(resultado=suma, comentarios="Durante el embarazo Una puntuación de 13 o más puntos indica sospecha de depresión.",
                                            user_id=id_user)
                guardar.save()
            elif (suma>= 10 and cuestionario[-1] =='Posparto'):
                guardar = resultdoEdimburgo(resultado=suma, comentarios="En el posparto una puntuación de 10 o más puntos indica sospecha de depresión posparto.",
                                            user_id=id_user)
                guardar.save()
            else:
                guardar = resultdoEdimburgo(resultado=suma, comentarios="No hay alerta de depresión",
                                            user_id=id_user)
                guardar.save()

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