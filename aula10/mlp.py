# Biblioteca
import numpy as np

# Funções auxiliares
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivada(x):
    return x * (1 - x)

# Dados de entrada (XOR)
entradas = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

saidas = np.array([[0], [1], [1], [0]])

# Inicialização dos pesos (valores aleatórios entre -1 e 1)
np.random.seed(42)
pesos_0 = 2 * np.random.rand(2, 4) - 1  # 2 entradas, 4 neurônios na camada oculta
pesos_1 = 2 * np.random.rand(4, 1) - 1  # 4 neurônios ocultos → 1 saída

# Treinamento
for epoca in range(1000):
    # Forward pass
    camada_0 = entradas # Entrada da rede
    camada_1 = sigmoid(np.dot(camada_0, pesos_0))  # Saída da camada oculta
    camada_2 = sigmoid(np.dot(camada_1, pesos_1))  # Saída final da rede

    # Cálculo do erro
    erro = saidas - camada_2

    # Impressão periódica do erro médio absoluto
    if epoca % 100 == 0:
        print(f'Época {epoca} - Erro médio: {np.mean(np.abs(erro)):.4f}')

    # Backpropagation
    delta_saida = erro * sigmoid_derivada(camada_2)
    delta_oculta = delta_saida.dot(pesos_1.T) * sigmoid_derivada(camada_1)

    # Atualização dos pesos
    pesos_1 += camada_1.T.dot(delta_saida)
    pesos_0 += camada_0.T.dot(delta_oculta)

# Resultados
print("\nSaídas previstas após o treinamento:")
print(np.round(camada_2))