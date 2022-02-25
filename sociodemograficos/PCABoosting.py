# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:14:16 2020

@author: Hallvaror
"""

import  numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

# =============================================================================
"""Ejemplo de lo que hace PCA"""

#mglearn.plots.plot_pca_illustration()

# =============================================================================

"""Importar Datset"""

dataset = pd.read_csv('sociodemograficos/dppDataSet.csv')

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=0)


from sklearn.preprocessing import  StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# =============================================================================
"""Reducir la dimensión del DataSet con PCA"""
from sklearn.decomposition import PCA, IncrementalPCA, KernelPCA
pca = PCA(n_components=3)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)


explained_variance = pca.explained_variance_ratio_

from sklearn.ensemble import AdaBoostClassifier
algoritmo = AdaBoostClassifier(n_estimators=50, learning_rate=1)
#algoritmo = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0).fit(X_train, y_train)

algoritmo.fit(X_train, y_train)


y_pred = algoritmo.predict(X_test)

y_score = algoritmo.decision_function(X_test)
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report, roc_auc_score, average_precision_score, plot_precision_recall_curve, auc, roc_curve, plot_roc_curve

matriz = confusion_matrix(y_test, y_pred)

average_precision = average_precision_score(y_test, y_score)

exactitud = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

sensibilidad = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

reporte = classification_report(y_test, y_pred)



vn = matriz[0][0]
fn =  matriz[1][0]
fp = matriz[0][1]
vp =  matriz[1][1]


especificidad = vn / (vn + fp)


#especificidad, sensibilidad, thresholds = roc_curve(y, y_test, pos_label=2)
#auc = auc(especificidad, sensibilidad)

plot_roc_curve(algoritmo, X_test, y_test)
plt.show()

disp = plot_precision_recall_curve(algoritmo, X_test, y_test)
disp.ax_.set_title('2-class Precision-Recall curve: '
                   'AP={0:0.2f}'.format(average_precision))