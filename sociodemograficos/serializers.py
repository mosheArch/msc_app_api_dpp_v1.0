from rest_framework import serializers
from core.models.model_datosSociodemograficos import DatosSociodemograficos, resultdoPrediccion


class datos_sociodemograficos_serializer(serializers.ModelSerializer):
    class Meta:
        model = DatosSociodemograficos
        #fields = '__all__'
        exclude = ['created']



class resultados_datos_sociodemograficos_serializer(serializers.ModelSerializer):
    class Meta:
        model = resultdoPrediccion
        fields = '__all__'