from rest_framework import viewsets, mixins, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models.model_datosSociodemograficos import DatosSociodemograficos, resultdoPrediccion
from sociodemograficos import serializers

import matplotlib.pyplot as plt
import pandas as pd


# data = open("sociodemograficos/dppDataSet.csv")

class DatosListsView_Sociodemograficos(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = DatosSociodemograficos.objects.all()
    serializer_class = serializers.datos_sociodemograficos_serializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('user_id')

    def post(self, request):
        # Importar Datset
        """Impotamos le dtaset con los usarios para el entrenamiento"""
        dataset = pd.read_csv('sociodemograficos/dppDataSet.csv')
        """Dividimos os datos en X y Y siendo Y la ultima columna a predecir"""
        X = dataset.iloc[:, :-1]
        y = dataset.iloc[:, -1]

        """Data serializada enviada desde el api"""
        serializer = serializers.datos_sociodemograficos_serializer(data=request.data)

        """Validación dea Data enviada desde el cliente"""
        if serializer.is_valid():
            """Si los datos son validos de guardan en BD"""
            serializer.save()
            """Obtengo el id del user para guardarloe n el modelo de resultados"""
            id = serializer.data.get('user')

            """Para poder meter datos en el algoritmo obtengo en un arreglo la lista de lso valores que vienen en el api"""
            dataset = serializer.data.values()

            """Convierto los datos de la lista o arreglo en  tipo float """
            datosSet = list(map(float, dataset))

            """Genereo un arreglo 2D"""
            datosSet = [datosSet]

            """Elimino del arreglo el id del registro y el id del user ya que el algoritmo esta esperando 24 valores en un arreglo 2D"""
            del datosSet[0][0]
            del datosSet[0][-1]

            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1, random_state=0)

            # Escalando la variable
            from sklearn.preprocessing import StandardScaler
            sc_X = StandardScaler()
            X_train = sc_X.fit_transform(X_train)
            X_test = sc_X.transform(X_test)

            datosSet = sc_X.transform(datosSet)  # ------------------------------------------------
            from sklearn.ensemble import AdaBoostClassifier
            algoritmo = AdaBoostClassifier(n_estimators=50, learning_rate=1)
            # algoritmo = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(X_train, y_train)

            algoritmo.fit(X_train, y_train)

            y_pred = algoritmo.predict(datosSet)

            y_score = algoritmo.decision_function(datosSet)
            from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, \
                classification_report, roc_auc_score, average_precision_score, plot_precision_recall_curve, auc, \
                roc_curve, plot_roc_curve
            # matriz = confusion_matrix(y_test, y_pred)

            precision = precision_score(y_test, y_pred)

            m = resultdoPrediccion(resultado=y_pred, user_id=id)
            m.save()

            return Response(y_pred)  # -------------------------------------------------------------------
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


class ResultadosListsView_Sociodemograficos(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = resultdoPrediccion.objects.all()
    serializer_class = serializers.resultados_datos_sociodemograficos_serializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('user_id')


class ResultadosDetailView_Sociodemograficos(generics.RetrieveAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = resultdoPrediccion.objects.all()
    serializer_class = serializers.resultados_datos_sociodemograficos_serializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('user_id')
