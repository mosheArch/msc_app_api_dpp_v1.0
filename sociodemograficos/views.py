from rest_framework import viewsets, mixins, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models.model_datosSociodemograficos import DatosSociodemograficos
from sociodemograficos import serializers

import matplotlib.pyplot as plt
import pandas as pd
#data = open("sociodemograficos/dppDataSet.csv")

class DatosListsView_Sociodemograficos(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = DatosSociodemograficos.objects.all()
    serializer_class = serializers.datos_sociodemograficos_serializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('user_id')

    def post(self, request):



        # Importar Datset

        dataset = pd.read_csv('sociodemograficos/dppDataSet.csv')
        X = dataset.iloc[:, :-1]
        y = dataset.iloc[:, -1]

        # Dividir el dataset entrenamiento y testing

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=20, random_state=0)

        # Escalando la variable

        from sklearn.preprocessing import StandardScaler
        sc_X = StandardScaler()
        X_train = sc_X.fit_transform(X_train)
        X_test = sc_X.transform(X_test)

        from sklearn.ensemble import AdaBoostClassifier
        algoritmo = AdaBoostClassifier(n_estimators=50, learning_rate=1)
        # algoritmo = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(X_train, y_train)

        algoritmo.fit(X_train, y_train)

        y_pred = algoritmo.predict(X_test)

        y_score = algoritmo.decision_function(X_test)
        from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, \
            classification_report, roc_auc_score, average_precision_score, plot_precision_recall_curve, auc, roc_curve, \
            plot_roc_curve
        #matriz = confusion_matrix(y_test, y_pred)

        precision = precision_score(y_test, y_pred)

        serializer = serializers.datos_sociodemograficos_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datosSet = serializer.data.values()

            return Response(datosSet)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DatosDetailView_Sociodemograficos(generics.RetrieveAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = DatosSociodemograficos.objects.all()
    serializer_class = serializers.datos_sociodemograficos_serializer
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('user_id')

    def put(self, request, pk):
        try:
            datos = DatosSociodemograficos.objects.get(pk=pk)
        except DatosSociodemograficos.DoesNotExist:
            return Response({'Error': 'El dato no existe'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.datos_sociodemograficos_serializer(datos, data=request.data)
        if serializer.is_valid() and self.queryset.filter(user=self.request.user).order_by('user_id'):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            datos = DatosSociodemograficos.objects.get(pk=pk)
        except DatosSociodemograficos.DoesNotExist:
            return Response({'Error': 'El dato no existe'}, status=status.HTTP_404_NOT_FOUND)

        if self.queryset.filter(user=self.request.user).order_by('user_id'):
            datos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# class DatosDetailView_Sociodemograficos(APIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request, pk):
#         try:
#             datos = DatosSociodemograficos.objects.get(pk=pk)
#         except DatosSociodemograficos.DoesNotExist:
#             return Response({'Error': 'El dato no existe'}, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = serializers.datos_sociodemograficos_serializer(datos)
#         return Response(serializer.data)
#
#
