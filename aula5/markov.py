"""
# M1
"""

# Biblioteca
import numpy as np

# Definindo os nomes dos estados para exibir
nomes_estados = ["Ensolarado", "Nublado", "Chuvoso"]

# Matriz de Transição
matriz = np.array([
    [0.7, 0.2, 0.1],  # De Ensolarado para {Ensolarado, Nublado, Chuvoso}
    [0.3, 0.4, 0.3],  # De Nublado para {Ensolarado, Nublado, Chuvoso}
    [0.2, 0.3, 0.5]   # De Chuvoso para {Ensolarado, Nublado, Chuvoso}
])

# Estado Inicial
estado_inicial = np.array([0.9, 0.1, 0.0])

# Função principal para simulação de Cadeia de Markov
def cadeia_markov(matriz, estado_inicial, periodos):

    estados = [estado_inicial]  # Lista para armazenar os estados ao longo do tempo

    for _ in range(periodos):
        # Multiplicação da matriz de transição pelo estado atual (vetor)
        novo_estado = np.dot(estados[-1], matriz)  # Multiplicação de matriz para o próximo estado
        estados.append(novo_estado)  # Adicionar o novo estado à lista

    # Converter lista para array NumPy para facilitar manipulação
    estados = np.array(estados).round(2)

    return estados

# Informar o número de períodos
periodos = int(input("Por favor, digite o número de períodos: "))

# Exibir os estados
simulacao = cadeia_markov(matriz, estado_inicial, periodos)

# Exibir os resultados
print("Estados simulados ao longo dos dias:")
for i, estado in enumerate(simulacao):
    print(f"Dia {i}:")
    for j, probabilidade in enumerate(estado):
        print(f"  {nomes_estados[j]}: {probabilidade}")
    print()  # Para separar os dias

"""# M2"""

# Biblioteca
import numpy as np

# Definindo os nomes dos estados para exibir
nomes_estados = ["Navegando", "No carrinho", "Comprando"]

# Matriz de Transição
matriz = np.array([
    [0.6, 0.3, 0.1],
    [0.1, 0.5, 0.4],
    [0.2, 0.1, 0.7]
])

# Estado Inicial
estado_inicial = np.array([0.5, 0.3, 0.2])

# Função principal para simulação de Cadeia de Markov
def cadeia_markov(matriz, estado_inicial, periodos):

    estados = [estado_inicial]  # Lista para armazenar os estados ao longo do tempo

    for _ in range(periodos):
        # Multiplicação da matriz de transição pelo estado atual (vetor)
        novo_estado = np.dot(estados[-1], matriz)  # Multiplicação de matriz para o próximo estado
        estados.append(novo_estado)  # Adicionar o novo estado à lista

    # Converter lista para array NumPy para facilitar manipulação
    estados = np.array(estados).round(4)

    return estados

# Informar o número de períodos
periodos = int(input("Por favor, digite o número de períodos: "))

# Exibir os estados
simulacao = cadeia_markov(matriz, estado_inicial, periodos)

# Exibir os resultados
print("Estados simulados ao longo das compras:")
for i, estado in enumerate(simulacao):
    print(f"Período {i}:")
    for j, probabilidade in enumerate(estado):
        print(f"  {nomes_estados[j]}: {probabilidade}")
    print()  # Para separar os dias

"""# M3"""

# Biblioteca
import numpy as np

# Definindo os nomes dos estados para exibir
nomes_estados = ["Estável", "Crítico", "Recuperado", "Óbito"]

# Estado Inicial
estado_inicial = np.array([0.7, 0.2, 0.1, 0.0])

# Matriz de Transição
matriz = np.array([
    [0.65, 0.15, 0.18, 0.02],
    [0.05, 0.40, 0.25, 0.30],
    [0.00, 0.00, 1.00, 0.00],
    [0.00, 0.00, 0.00, 1.00]
])

# Função principal para simulação de Cadeia de Markov
def cadeia_markov(matriz, estado_inicial, periodos):

    estados = [estado_inicial]  # Lista para armazenar os estados ao longo do tempo

    for _ in range(periodos):
        # Multiplicação da matriz de transição pelo estado atual (vetor)
        novo_estado = np.dot(estados[-1], matriz)  # Multiplicação de matriz para o próximo estado
        estados.append(novo_estado)  # Adicionar o novo estado à lista

    # Converter lista para array NumPy para facilitar manipulação
    estados = np.array(estados).round(4)

    return estados

# Informar o número de períodos
periodos = int(input("Por favor, digite o número de períodos: "))

# Exibir os estados
simulacao = cadeia_markov(matriz, estado_inicial, periodos)

# Exibir os resultados
print("Períodos:")
for i, estado in enumerate(simulacao):
    print(f"Período {i}:")
    for j, probabilidade in enumerate(estado):
        print(f"  {nomes_estados[j]}: {probabilidade}")
    print()  # Para separar os dias