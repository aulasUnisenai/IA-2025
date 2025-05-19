'''
# Instalar a biblioteca (Colab)
!pip install scikit-fuzzy
'''

# Bibliotecas
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Variáveis fuzzy
nota = ctrl.Antecedent(np.arange(0, 11, 1), 'nota')  # Nota do trabalho (0 a 10)
clareza = ctrl.Consequent(np.arange(0, 11, 1), 'clareza')  # Clareza do trabalho (0 a 10)

# 2. Conjuntos fuzzy para nota (funções trapezoidais)
nota['ruim'] = fuzz.trapmf(nota.universe, [0, 0, 3, 5])
nota['boa'] = fuzz.trapmf(nota.universe, [3, 5, 7, 9])
nota['excelente'] = fuzz.trapmf(nota.universe, [7, 9, 10, 10])

# 3. Conjuntos fuzzy para clareza (funções trapezoidais)
clareza['ruim'] = fuzz.trapmf(clareza.universe, [0, 0, 3, 5])
clareza['boa'] = fuzz.trapmf(clareza.universe, [3, 5, 7, 9])
clareza['excelente'] = fuzz.trapmf(clareza.universe, [7, 9, 10, 10])

# 4. Regras fuzzy
regra1 = ctrl.Rule(nota['ruim'], clareza['ruim'])  # Se a nota for ruim, clareza será ruim
regra2 = ctrl.Rule(nota['boa'], clareza['boa'])  # Se a nota for boa, clareza será boa
regra3 = ctrl.Rule(nota['excelente'], clareza['excelente'])  # Se a nota for excelente, clareza será excelente

# 5. Sistema de controle fuzzy
sistema = ctrl.ControlSystem([regra1, regra2, regra3])
simulador = ctrl.ControlSystemSimulation(sistema)

# 6. Função para exibir regras e gráficos
def regras_ativas():
    try:
        n = float(input("Digite a nota (0 a 10): "))
        if n < nota.universe[0] or n > nota.universe[-1]:
            print("Nota inválida. Digite um valor entre 0 e 10.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    print(f"\nNota: {n}")

    # Graus de pertinência para 'nota'
    grau_ruim = fuzz.interp_membership(nota.universe, nota['ruim'].mf, n)
    grau_boa = fuzz.interp_membership(nota.universe, nota['boa'].mf, n)
    grau_excelente = fuzz.interp_membership(nota.universe, nota['excelente'].mf, n)

    print("\nRegras ativas:")
    if grau_ruim > 0:
        print(f" → Regra 1: nota baixa → clareza baixa (grau de ativação: {grau_ruim:.2%})")
    if grau_boa > 0:
        print(f" → Regra 2: nota média → clareza média (grau de ativação: {grau_boa:.2%})")
    if grau_excelente > 0:
        print(f" → Regra 3: nota alta → clareza alta (grau de ativação: {grau_excelente:.2%})")

    # Define o valor de entrada e calcula
    simulador.input['nota'] = n
    simulador.compute()

    # Mostra o resultado numérico
    clareza_resultado = simulador.output['clareza']
    print(f"\nResultado fuzzy: Clareza = {clareza_resultado:.2f}")

    # Gráficos
    print("\nExibindo gráficos dos conjuntos fuzzy...")
    nota.view(sim=simulador)
    clareza.view(sim=simulador)

# Chamar a função
regras_ativas()