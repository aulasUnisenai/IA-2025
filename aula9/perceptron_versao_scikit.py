# Bibliotecas
from sklearn.linear_model import Perceptron
import numpy as np

# Dados de entrada (x1, x2)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Saída desejada (AND)
y = np.array([0, 1, 1, 1])

# Criação do modelo Perceptron
modelo = Perceptron(max_iter=10, eta0=0.1, random_state=0)

# Treinamento
modelo.fit(X, y)

# Teste
y_pred = modelo.predict(X)

# Resultados
print("Pesos:", modelo.coef_)
print("Bias:", modelo.intercept_)
print("Saída real:", y)
print("Saída prevista:", y_pred)