# -*- coding: utf-8 -*-
"""
# A* - 1
"""

# Implementar fila de prioridade
import heapq

# Grafo (distâncias entre as cidades)
grafo = {
    'A': {'B': 10, 'C': 15, 'D': 20,  'E': 30},
    'B': {'A': 10, 'C': 35, 'D': 25,  'E': 40},
    'C': {'A': 15, 'B': 25, 'D': 30,  'E': 50},
    'D': {'A': 20, 'B': 25,  'C': 30,  'E': 10},
    'E': {'A': 30, 'B':40,  'C':50,   'D':10}
}

# Heurísticas
heuristica = {
    'A': 20,
    'B': 25,
    'C': 30,
    'D': 5,
    'E': 0
}

# Função principal
def a_star(grafo, heuristica, inicio, destino):
  '''
  (f, g, nó_atual, caminho_percorrido)
  heuristica[inicio]: Estimativa inicial do custo ao destino
  0: Custo acumulado até o momento
  inicio: O nó de partida
  [inicio]: Caminho percorrido até agora
  '''
  fila, visitados = [(heuristica[inicio], 0, inicio, [inicio])], set()


  # Enquanto tiver fila
  while fila:
    _, g, atual, caminho = heapq.heappop(fila) # Retirar o nó com menor f
    # Se o nó já foi explorado, ignorar
    if atual in visitados:
      continue
    # Se destino, retornar caminho encontrado e o custo total
    if atual == destino:
      return caminho, g
    visitados.add(atual) # Adicionar aos visitados

    # Percorrer todos os vizinhos do nó atual e seus custos
    for  vizinho, custo in grafo[atual].items():
      # Se o vizinho não foi visitado, explorar
      if vizinho not in visitados:
        heapq.heappush(fila, (g + custo + heuristica[vizinho],
                              g + custo, vizinho,
                              caminho + [vizinho]))
  return None, float('inf')

resultado = a_star(grafo, heuristica, "A", "E")
print(resultado)

"""# A* - 2"""

# Implementar fila de prioridade
import heapq

# Definição do grafo (distâncias reais entre cidades)
grafo = {
    'SP': {'RJ': 300, 'BH': 450, 'BSB': 700, 'CWB': 350, 'SSA': 1800},
    'RJ': {'SP': 300, 'BH': 200, 'BSB': 800, 'CWB': 500, 'SSA': 1500},
    'BH': {'SP': 450, 'RJ': 200, 'BSB': 600, 'CWB': 800, 'SSA': 1200},
    'BSB': {'SP': 700, 'RJ': 800, 'BH': 600, 'CWB': 900, 'SSA': 1100},
    'CWB': {'SP': 350, 'RJ': 500, 'BH': 800, 'BSB': 900, 'SSA': 2000},
    'SSA': {'SP': 1800, 'RJ': 1500, 'BH': 1200, 'BSB': 1100, 'CWB': 2000}
}

# Heurísticas: estimativa até o objetivo (SSA)
heuristica = {
    'SP': 1500,
    'RJ': 1200,
    'BH': 900,
    'BSB': 1100,
    'CWB': 1700,
    'SSA': 0
}

# Função principal
def a_star(grafo, heuristica, inicio, destino):
  '''
  (f, g, nó_atual, caminho_percorrido)
  heuristica[inicio]: Estimativa inicial do custo ao destino
  0: Custo acumulado até o momento
  inicio: O nó de partida
  [inicio]: Caminho percorrido até agora
  '''
  fila, visitados = [(heuristica[inicio], 0, inicio, [inicio])], set()


  # Enquanto tiver fila
  while fila:
    _, g, atual, caminho = heapq.heappop(fila) # Retirar o nó com menor f
    # Se o nó já foi explorado, ignorar
    if atual in visitados:
      continue
    # Se destino, retornar caminho encontrado e o custo total
    if atual == destino:
      return caminho, g
    visitados.add(atual) # Adicionar aos visitados

    # Percorrer todos os vizinhos do nó atual e seus custos
    for  vizinho, custo in grafo[atual].items():
      # Se o vizinho não foi visitado, explorar
      if vizinho not in visitados:
        heapq.heappush(fila, (g + custo + heuristica[vizinho],
                              g + custo, vizinho,
                              caminho + [vizinho]))
  return None, float('inf')

resultado = a_star(grafo, heuristica, "SP", "SSA" )
print(resultado)