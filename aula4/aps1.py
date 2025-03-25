# -*- coding: utf-8 -*-
"""
# BFS-1
"""

# Biblioteca
from collections import deque

# Grafo representado como um dicionário de adjacências
grafo = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': ['A']
}

# Função principal
def bfs(grafo, inicio):
    fila = deque([inicio])  # Fila
    visitado = set([inicio])  # Conjunto para evitar visitas repetidas
    ordem = []  # Lista para registrar a ordem de visitação

    while fila:
        atual = fila.popleft()  # Remove o primeiro elemento da fila
        ordem.append(atual)  # Registra a visita

        # Adiciona os vizinhos não visitados na fila
        for vizinho in grafo.get(atual, []):
            if vizinho not in visitado:
                fila.append(vizinho)
                visitado.add(vizinho)  # Marca como visitado

    return ordem  # Retorna a ordem de visitação

# Executa o BFS a partir do nó escolhido
pontos = ['A', 'B', 'C','D']

for ponto in pontos:
    resultado = bfs(grafo, ponto)
    print("Ordem BFS:", resultado)

"""# BFS-2"""

# Biblioteca
from collections import deque

# Grafo
grafo = {
    'A': ['B', 'E'],
    'B': ['C'],
    'C': ['D', 'E'],
    'D': ['C'],
    'E': ['A']
}

# Função principal
def bfs(grafo, inicio):
    fila = deque([inicio])  # Fila
    visitado = set([inicio])  # Conjunto para evitar visitas repetidas
    ordem = []  # Lista para registrar a ordem de visitação

    while fila:
        atual = fila.popleft()  # Remove o primeiro elemento da fila
        ordem.append(atual)  # Registra a visita

        # Adiciona os vizinhos não visitados na fila
        for vizinho in grafo.get(atual, []):
            if vizinho not in visitado:
                fila.append(vizinho)
                visitado.add(vizinho)  # Marca como visitado

    return ordem  # Retorna a ordem de visitação

# Executa o BFS a partir do nó escolhido
pontos = ['A', 'B', 'C','D','E']

for ponto in pontos:
    resultado = bfs(grafo, ponto)
    print("Ordem BFS:", resultado)

"""# BFS-3"""

# Biblioteca
from collections import deque

# Grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D'],
    'F': ['G'],  # Componente separado
    'G': ['F']
}

# Função principal
def bfs(grafo, inicio):
    fila = deque([inicio])  # Fila
    visitado = set([inicio])  # Conjunto para evitar visitas repetidas
    ordem = []  # Lista para registrar a ordem de visitação

    while fila:
        atual = fila.popleft()  # Remove o primeiro elemento da fila
        ordem.append(atual)  # Registra a visita

        # Adiciona os vizinhos não visitados na fila
        for vizinho in grafo.get(atual, []):
            if vizinho not in visitado:
                fila.append(vizinho)
                visitado.add(vizinho)  # Marca como visitado

    return ordem  # Retorna a ordem de visitação

# Executa o BFS a partir do nó escolhido
pontos = ['A', 'B', 'C','D','E', 'F', 'G']

for ponto in pontos:
    resultado = bfs(grafo, ponto)
    print("Ordem BFS:", resultado)

"""# BFS - 4"""

# Biblioteca
from collections import deque

grafo = {
    'Aatrox': ['Yasuo', 'Zed', 'Riven'],
    'Yasuo': ['Aatrox', 'Riven', 'Zed', 'Leona', 'Lux'],
    'Zed': ['Yasuo', 'Aatrox', 'Riven', 'Thresh'],
    'Riven': ['Aatrox', 'Yasuo', 'Zed', 'Leona', 'Lux'],
    'Leona': ['Yasuo', 'Riven', 'Thresh', 'Lux'],
    'Lux': ['Yasuo', 'Riven', 'Leona', 'Jinx'],
    'Thresh': ['Yasuo', 'Zed', 'Leona'],
    'Jinx': ['Yasuo', 'Zed', 'Leona', 'Thresh'],
}

# Função principal
def bfs(grafo, inicio):
    fila = deque([inicio])  # Fila
    visitado = set([inicio])  # Conjunto para evitar visitas repetidas
    ordem = []  # Lista para registrar a ordem de visitação

    while fila:
        atual = fila.popleft()  # Remove o primeiro elemento da fila
        ordem.append(atual)  # Registra a visita

        # Adiciona os vizinhos não visitados na fila
        for vizinho in grafo.get(atual, []):
            if vizinho not in visitado:
                fila.append(vizinho)
                visitado.add(vizinho)  # Marca como visitado

    return ordem  # Retorna a ordem de visitação

# Executa o BFS a partir do nó escolhido
pontos = ['Aatrox', 'Yasuo',    'Zed',  'Riven',    'Leona',    'Lux',  'Thresh',   'Jinx']

for ponto in pontos:
    resultado = bfs(grafo, ponto)
    print("Ordem BFS:", resultado)

"""# BFS - 5"""

# Biblioteca
from collections import deque

grafo  = {
    'Restaurante Japonês': ['Restaurante Mexicano', 'Restaurante Chinês', 'Restaurante Italiano', 'Restaurante Árabe'],
    'Restaurante Mexicano': ['Restaurante Brasileiro', 'Restaurante Italiano', 'Restaurante Japonês', 'Restaurante Fast Food'],
    'Restaurante Chinês': ['Restaurante Mediterrâneo', 'Restaurante Mexicano', 'Restaurante Japonês', 'Restaurante Thai'],
    'Restaurante Brasileiro': ['Restaurante Italiano', 'Restaurante Chinês', 'Restaurante Fast Food', 'Restaurante Árabe'],
    'Restaurante Italiano': ['Restaurante Mediterrâneo', 'Restaurante Japonês', 'Restaurante Mexicano', 'Restaurante Brasileiro'],
    'Restaurante Mediterrâneo': ['Restaurante Brasileiro', 'Restaurante Italiano', 'Restaurante Chinês', 'Restaurante Thai'],
    'Restaurante Thai': ['Restaurante Chinês', 'Restaurante Mediterrâneo', 'Restaurante Árabe', 'Restaurante Japonês'],
    'Restaurante Árabe': ['Restaurante Italiano', 'Restaurante Mexicano', 'Restaurante Fast Food', 'Restaurante Thai'],
    'Restaurante Fast Food': ['Restaurante Brasileiro', 'Restaurante Mediterrâneo', 'Restaurante Mexicano', 'Restaurante Árabe']
}

# Função principal
def bfs(grafo, inicio):
    fila = deque([inicio])  # Fila
    visitado = set([inicio])  # Conjunto para evitar visitas repetidas
    ordem = []  # Lista para registrar a ordem de visitação

    while fila:
        atual = fila.popleft()  # Remove o primeiro elemento da fila
        ordem.append(atual)  # Registra a visita

        # Adiciona os vizinhos não visitados na fila
        for vizinho in grafo.get(atual, []):
            if vizinho not in visitado:
                fila.append(vizinho)
                visitado.add(vizinho)  # Marca como visitado

    return ordem  # Retorna a ordem de visitação

# Executa o BFS a partir do nó escolhido
pontos = ['Restaurante Japonês', 'Restaurante Mexicano', 'Restaurante Chinês',
          'Restaurante Brasileiro', 'Restaurante Italiano', 'Restaurante Mediterrâneo',
          'Restaurante Thai', 'Restaurante Árabe', 'Restaurante Fast Food']

for ponto in pontos:
    resultado = bfs(grafo, ponto)
    print("Ordem BFS:", resultado)

"""# A* 1"""

# Implementar uma fila de prioridade
import heapq

# Definir grafo (distâncias reais entre cidades)
grafo = {
    "Foz do Iguaçu": {"Cascavel": 140, "Toledo": 100, "Francisco Beltrão": 160, "Guarapuava": 250, "Ponta Grossa": 320, "Curitiba": 600, "Piraquara": 670},
    "Cascavel": {"Foz do Iguaçu": 140, "Toledo": 50, "Francisco Beltrão": 120, "Guarapuava": 180, "Ponta Grossa": 240, "Curitiba": 550, "Piraquara": 620},
    "Toledo": {"Foz do Iguaçu": 100, "Cascavel": 50, "Francisco Beltrão": 90, "Guarapuava": 150, "Ponta Grossa": 220, "Curitiba": 540, "Piraquara": 610},
    "Francisco Beltrão": {"Foz do Iguaçu": 160, "Cascavel": 120, "Toledo": 90, "Guarapuava": 100, "Ponta Grossa": 170, "Curitiba": 480, "Piraquara": 550},
    "Guarapuava": {"Foz do Iguaçu": 250, "Cascavel": 180, "Toledo": 150, "Francisco Beltrão": 100, "Ponta Grossa": 100, "Curitiba": 350, "Piraquara": 420},
    "Ponta Grossa": {"Foz do Iguaçu": 320, "Cascavel": 240, "Toledo": 220, "Francisco Beltrão": 170, "Guarapuava": 100, "Curitiba": 140, "Piraquara": 210},
    "Curitiba": {"Foz do Iguaçu": 600, "Cascavel": 550, "Toledo": 540, "Francisco Beltrão": 480, "Guarapuava": 350, "Ponta Grossa": 140, "Piraquara": 80},
    "Piraquara": {"Foz do Iguaçu": 670, "Cascavel": 620, "Toledo": 610, "Francisco Beltrão": 550, "Guarapuava": 420, "Ponta Grossa": 210, "Curitiba": 80},
}

heuristicas = {
    "Foz do Iguaçu": 670,
    "Cascavel": 620,
    "Toledo": 610,
    "Francisco Beltrão": 550,
    "Guarapuava": 420,
    "Ponta Grossa": 210,
    "Curitiba": 80,
    "Piraquara": 0,
}

# Função principal
def a_star(grafo, heuristica, inicio, destino):
    '''
    (f, g, nó_atual, caminho_percorrido)
    heuristica[inicio]: Estimativa inicial do custo ao destino.
    0: Custo acumulado até o momento.
    inicio: O nó de partida.
    [inicio]: Caminho percorrido até agora.
    '''
    fila, visitados = [(heuristica[inicio], 0, inicio, [inicio])], set()

    # Enquanto houver fila
    while fila:
        _, g, atual, caminho = heapq.heappop(fila) #  Retirar o nó com o menor valor de f
        # Se o nó já foi explorado antes, ignorar.
        if atual in visitados:
            continue
        #Se destino, retornar o caminho encontrado e o custo total.
        if atual == destino:
            return caminho, g
        visitados.add(atual) # O nó atual é adicionado ao conjunto de nós visitados.

        # Percorrer todos os vizinhos do nó atual e seus respectivos custos.
        for vizinho, custo in grafo[atual].items():
            # Se o vizinho ainda não foi visitado, ele é considerado para exploração.
            if vizinho not in visitados:
                # Adicionar o vizinho na fila de prioridade
                heapq.heappush(fila, (g + custo + heuristica[vizinho],
                                      g + custo, vizinho,
                                      caminho + [vizinho]))

    # Se não for possível alcançar o destino, retorna None e um custo infinito (float("inf")).
    return None, float("inf")

inicio = input("Digite o ponto de partida: ")
destino = input("Digite o destino: ")
caminho, custo = a_star(grafo, heuristicas, inicio, destino)
print(f"Caminho: {caminho}, Custo: {custo}")

"""# A* 2"""

# Implementar uma fila de prioridade
import heapq

grafo = {
    "Ribeirão Preto": {"São Carlos": 75, "Araraquara": 70, "Matão": 85, "Jaú": 120, "São Paulo": 330, "Pindamonhangaba": 270},
    "São Carlos": {"Ribeirão Preto": 75, "Araraquara": 35, "Matão": 40, "Jaú": 85, "São Paulo": 235, "Pindamonhangaba": 200},
    "Araraquara": {"Ribeirão Preto": 70, "São Carlos": 35, "Matão": 25, "Jaú": 55, "São Paulo": 210, "Pindamonhangaba": 180},
    "Matão": {"Ribeirão Preto": 85, "São Carlos": 40, "Araraquara": 25, "Jaú": 60, "São Paulo": 220, "Pindamonhangaba": 190},
    "Jaú": {"Ribeirão Preto": 120, "São Carlos": 85, "Araraquara": 55, "Matão": 60, "São Paulo": 170, "Pindamonhangaba": 150},
    "São Paulo": {"Ribeirão Preto": 330, "São Carlos": 235, "Araraquara": 210, "Matão": 220, "Jaú": 170, "Pindamonhangaba": 140},
    "Pindamonhangaba": {"Ribeirão Preto": 270, "São Carlos": 200, "Araraquara": 180, "Matão": 190, "Jaú": 150, "São Paulo": 140},
}

heuristicas = {
    "Ribeirão Preto": 270,
    "São Carlos": 200,
    "Araraquara": 180,
    "Matão": 190,
    "Jaú": 150,
    "São Paulo": 140,
    "Pindamonhangaba": 0,
}

# Função principal
def a_star(grafo, heuristica, inicio, destino):
    '''
    (f, g, nó_atual, caminho_percorrido)
    heuristica[inicio]: Estimativa inicial do custo ao destino.
    0: Custo acumulado até o momento.
    inicio: O nó de partida.
    [inicio]: Caminho percorrido até agora.
    '''
    fila, visitados = [(heuristica[inicio], 0, inicio, [inicio])], set()

    # Enquanto houver fila
    while fila:
        _, g, atual, caminho = heapq.heappop(fila) #  Retirar o nó com o menor valor de f
        # Se o nó já foi explorado antes, ignorar.
        if atual in visitados:
            continue
        #Se destino, retornar o caminho encontrado e o custo total.
        if atual == destino:
            return caminho, g
        visitados.add(atual) # O nó atual é adicionado ao conjunto de nós visitados.

        # Percorrer todos os vizinhos do nó atual e seus respectivos custos.
        for vizinho, custo in grafo[atual].items():
            # Se o vizinho ainda não foi visitado, ele é considerado para exploração.
            if vizinho not in visitados:
                # Adicionar o vizinho na fila de prioridade
                heapq.heappush(fila, (g + custo + heuristica[vizinho],
                                      g + custo, vizinho,
                                      caminho + [vizinho]))

    # Se não for possível alcançar o destino, retorna None e um custo infinito (float("inf")).
    return None, float("inf")

inicio = input("Digite o ponto de partida: ")
destino = input("Digite o destino: ")
caminho, custo = a_star(grafo, heuristicas, inicio, destino)
print(f"Caminho: {caminho}, Custo: {custo}")