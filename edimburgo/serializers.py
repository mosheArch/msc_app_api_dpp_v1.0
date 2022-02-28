from rest_framework import serializers
from core.models.model_edimburgo import CuestionarioEdimburgo, resultdoEdimburgo


class datos_cuestionarioEdimburgo_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = CuestionarioEdimburgo

        exclude = ['created']

class resultados_cuestionarioEdimburgo_serializer(serializers.ModelSerializer):

    class Meta:
        model = resultdoEdimburgo
        exclude = ['created']