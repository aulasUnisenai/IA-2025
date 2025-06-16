# Métricas de classificação

# Biblioteca
from sklearn.metrics import (accuracy_score,
                             precision_score,
                             recall_score,
                             f1_score,
                             confusion_matrix)

# Dados de exemplo
y = [0, 1, 0, 1, 0, 1]
y_pred = [0, 0, 0, 1, 0, 1]

print("Métricas de Classificação:")
# Acurácia: proporção de acertos totais
print(f"Acurácia: {accuracy_score(y, y_pred):.2f}")
# Precisão: dos que foram classificados como positivos, quantos realmente são
print(f"Precisão: {precision_score(y, y_pred):.2f}")
# Revocação: dos positivos reais, quantos o modelo encontrou
print(f"Revocação: {recall_score(y, y_pred):.2f}")
# F1-Score: equilíbrio entre precisão e revocação
print(f"F1-Score: {f1_score(y, y_pred):.2f}")

# Síntese
from sklearn.metrics import classification_report
print(classification_report(y, y_pred))

# Matriz de confusão: acertos e erros por classe
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(confusion_matrix(y, y_pred),
            annot=True, fmt='d', cmap='Blues')
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.title("Matriz de Confusão")
plt.show()

"""# Métricas de regressão"""

# Biblioteca
from sklearn.metrics import (mean_absolute_error,
                             mean_squared_error,
                             r2_score)

# Dados de exemplo
y = [3.0, -0.5, 2.0, 7.0]
y_pred = [2.5, 0.0, 2.0, 8.0]

print("\nMétricas de Regressão:")
# Erro médio absoluto, fácil de interpretar
print(f"MAE: {mean_absolute_error(y, y_pred):.2f}")
# Penaliza mais os erros grandes, sensível a outliers
print(f"MSE: {mean_squared_error(y, y_pred):.2f}")
# Mede o quanto o modelo explica da variância dos dados
print(f"R²: {r2_score(y, y_pred):.2f}")

"""# Pré-processamento básico"""

from sklearn.preprocessing import (StandardScaler,
                                   MinMaxScaler)
import numpy as np

# Dados
X = [[1, -1, 2],
     [2, 0, 0],
     [0, 1, -1]]

print(X)

# Transforma para média 0 e desvio 1 (padrão para MLP)
scaler_std = StandardScaler()
X_std = scaler_std.fit_transform(X)
print("StandardScaler (média 0, desvio 1):")
print(X_std)

# Normaliza para intervalo [0, 1] (útil para redes ou distâncias)
scaler_minmax = MinMaxScaler()
X_minmax = scaler_minmax.fit_transform(X)
print("MinMaxScaler (normalização 0-1):")
print(X_minmax)