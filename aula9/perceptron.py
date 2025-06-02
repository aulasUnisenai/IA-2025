# Biblioteca necessária
import numpy as np

# Dados de entrada e saída esperada
entradas = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
saidas = np.array([0, 0, 0, 1])

# Parâmetros
pesos = np.random.uniform(-1, 1, 2)  # pesos aleatórios
bias = np.random.uniform(-1, 1)      # bias aleatório
taxa_aprendizado = 0.1
épocas = 100

# Função degrau
def step(soma):
    return 1 if soma >= 0 else 0

# Treinamento
for epoca in range(épocas):
    erro_total = 0
    for i in range(len(entradas)):
        x = entradas[i]
        y = saidas[i]

        soma = np.dot(x, pesos) + bias
        y_pred = step(soma)
        erro = y - y_pred

        # Atualização dos pesos e bias
        pesos += taxa_aprendizado * erro * x
        bias += taxa_aprendizado * erro
        erro_total += abs(erro)

    print(f'Época {epoca+1} - Erro total: {erro_total}')
    if erro_total == 0:
        break

# Impressão em formato de tabela
print("\nPesos finais:", pesos)
print("Bias final:", bias)
print("\nResultado final - Tabela de verdade aprendida:")
print("x1 | x2 | Soma   | y_real | y_previsto")
print(50*"-")
for i in range(len(entradas)):
    x = entradas[i]
    y = saidas[i]
    soma = np.dot(x, pesos) + bias
    y_pred = step(soma)
    print(f" {x[0]}  | {x[1]}  | {soma:6.2f} |   {y}    |     {y_pred}")