from rest_framework import serializers
from core.models.model_edimburgo import CuestionarioEdimburgo


class datos_cuestionarioEdimburgo_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = CuestionarioEdimburgo

        exclude = ['created']