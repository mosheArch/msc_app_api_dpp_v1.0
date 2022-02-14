from rest_framework import serializers
from core.models.model_datosSociodemograficos import DatosSociodemograficos


class datos_sociodemograficos_serializer(serializers.ModelSerializer):
    class Meta:
        model = DatosSociodemograficos
        #fields = '__all__'
        exclude = ['id', 'created']