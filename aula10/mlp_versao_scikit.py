# Bibliotecas
from sklearn.neural_network import MLPClassifier
import numpy as np

# Dados XOR
entradas = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

saidas = np.array([0, 1, 1, 0])

# Modelo MLP com 1 camada oculta de 3 neurônios
modelo = MLPClassifier(
    hidden_layer_sizes=(3,),
    activation='tanh', # Função de ativação tangente hiperbólica
    max_iter=10000,
    random_state=42
)
modelo.fit(entradas, saidas)

# Previsões
print("Saídas previstas:", modelo.predict(entradas))
print("Precisão:", modelo.score(entradas, saidas))