'''
# Instalar a biblioteca (Colab)
!pip install scikit-fuzzy
'''

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir as variáveis fuzzy
luminosidade = ctrl.Antecedent(np.arange(0, 101, 1), 'luminosidade')
intensidade_luz = ctrl.Consequent(np.arange(0, 101, 1), 'intensidade_luz')

# Definir as funções de pertinência para a luminosidade (entrada)
luminosidade['baixa'] = fuzz.sigmf(luminosidade.universe, 50, -0.1)  # Função sigmoide com c = -0.1
luminosidade['media'] = fuzz.sigmf(luminosidade.universe, 50, 0)     # Função sigmoide com c = 0
luminosidade['alta'] = fuzz.sigmf(luminosidade.universe, 50, 0.1)     # Função sigmoide com c = 0.1

# Definir as funções de pertinência para a intensidade da luz (saída)
intensidade_luz['baixa'] = fuzz.sigmf(intensidade_luz.universe, 50, -0.1)
intensidade_luz['media'] = fuzz.sigmf(intensidade_luz.universe, 50, 0)
intensidade_luz['alta'] = fuzz.sigmf(intensidade_luz.universe, 50, 0.1)

# Definir as regras fuzzy
regra1 = ctrl.Rule(luminosidade['baixa'], intensidade_luz['baixa'])
regra2 = ctrl.Rule(luminosidade['media'], intensidade_luz['media'])
regra3 = ctrl.Rule(luminosidade['alta'], intensidade_luz['alta'])

# Sistema de controle fuzzy
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
simulador = ctrl.ControlSystemSimulation(sistema_controle)

# Função para verificar as regras ativas e computar o valor da intensidade
def regras_ativas_fuzzy():
    n = float(input("Digite o valor da luminosidade (0 a 100): "))

    # Verificar intervalo
    if n < luminosidade.universe[0] or n > luminosidade.universe[-1]:
        print(f"Valor fora do intervalo válido ({luminosidade.universe[0]} a {luminosidade.universe[-1]}).")
        return

    print(f"\nLuminosidade: {n}")

    # Graus de pertinência para luminosidade
    grau_baixa = fuzz.interp_membership(luminosidade.universe, luminosidade['baixa'].mf, n)
    grau_media = fuzz.interp_membership(luminosidade.universe, luminosidade['media'].mf, n)
    grau_alta = fuzz.interp_membership(luminosidade.universe, luminosidade['alta'].mf, n)

    print("\nRegras ativas:")
    if grau_baixa > 0:
        print(f" → Regra 1: luminosidade baixa → intensidade baixa (grau de ativação: {grau_baixa:.2%})")
    if grau_media > 0:
        print(f" → Regra 2: luminosidade média → intensidade média (grau de ativação: {grau_media:.2%})")
    if grau_alta > 0:
        print(f" → Regra 3: luminosidade alta → intensidade alta (grau de ativação: {grau_alta:.2%})")

    simulador.input['luminosidade'] = n
    simulador.compute()

    intensidade_resultado = simulador.output['intensidade_luz']
    print(f"\nResultado fuzzy: Intensidade da luz = {intensidade_resultado:.2f}")


    print("\nExibindo gráficos dos conjuntos fuzzy...")
    luminosidade.view(sim=simulador)
    intensidade_luz.view(sim=simulador)

regras_ativas_fuzzy()