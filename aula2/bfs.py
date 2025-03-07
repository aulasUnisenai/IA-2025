# 1
# Biblioteca
from collections import deque

# Grafo representado como um dicionário de adjacências
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
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
        for v in grafo.get(atual, []):
            if v not in visitado:
                fila.append(v)
                visitado.add(v)  # Marca como visitado

    return ordem  # Retorna a ordem de visitação

# Executa o BFS a partir do nó escolhido
resultado = bfs(grafo, 'E')
print("Ordem BFS:", resultado)

"""# 2"""

# Biblioteca
from collections import deque

# Grafo representado como um dicionário de adjacências
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E', 'I'],
    'E': ['B', 'D', 'F'],
    'F': ['E', 'G', 'H', 'I', 'J'],
    'G': ['F', 'H', 'I'],
    'H': ['F', 'G', 'J'],
    'I': ['D', 'F', 'G', 'J'],
    'J': ['F', 'H', 'I']
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
        for v in grafo.get(atual, []):
            if v not in visitado:
                fila.append(v)
                visitado.add(v)  # Marca como visitado

    return ordem  # Retorna a ordem de visitação

# Executa o BFS a partir do nó escolhido
resultado = bfs(grafo, 'A')
print("Ordem BFS:", resultado)

"""# 3"""

from collections import deque

# Representação do grafo usando dicionário de listas de adjacência
grafo = {
    "Centro": ["Afonso Pena", "Costeira", "Boneca do Iguaçu"],
    "Afonso Pena": ["Centro", "São Domingos", "Guatupê"],
    "São Domingos": ["Afonso Pena", "Braga"],
    "Costeira": ["Centro", "Guatupê", "Iná"],
    "Guatupê": ["Afonso Pena", "Costeira", "Campo Largo da Roseira"],
    "Braga": ["São Domingos"],
    "Iná": ["Costeira"],
    "Boneca do Iguaçu": ["Centro"],
    "Campo Largo da Roseira": ["Guatupê"]
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
        for v in grafo.get(atual, []):
            if v not in visitado:
                fila.append(v)
                visitado.add(v)  # Marca como visitado

    return ordem  # Retorna a ordem de visitação

# Executando BFS a partir de "Centro"
caminho = bfs(grafo, "Centro")
print("Ordem de visitação (BFS) a partir do Centro:", " → ".join(caminho))