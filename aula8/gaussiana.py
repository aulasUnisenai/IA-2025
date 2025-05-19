'''
# Instalar a biblioteca (Colab)
!pip install scikit-fuzzy
'''

# Bibliotecas
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

nota = ctrl.Antecedent(np.arange(0, 11, 0.1), 'nota')
atencao = ctrl.Consequent(np.arange(0, 11, 0.1), 'atencao')

nota['baixa'] = fuzz.gaussmf(nota.universe, 2, 1)
nota['media'] = fuzz.gaussmf(nota.universe, 5, 1)
nota['alta'] = fuzz.gaussmf(nota.universe, 8, 1)

atencao['distraido'] = fuzz.gaussmf(atencao.universe, 2, 1)
atencao['atento'] = fuzz.gaussmf(atencao.universe, 5, 1)
atencao['focado'] = fuzz.gaussmf(atencao.universe, 8, 1)

regra1 = ctrl.Rule(nota['baixa'], atencao['distraido'])
regra2 = ctrl.Rule(nota['media'], atencao['atento'])
regra3 = ctrl.Rule(nota['alta'], atencao['focado'])

sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
simulador = ctrl.ControlSystemSimulation(sistema_controle)

def regras_ativas_gaussiana():
    n = float(input("Digite a nota (0 a 10): "))

    if n < nota.universe[0] or n > nota.universe[-1]:
        print(f"Valor fora do intervalo válido ({nota.universe[0]} a {nota.universe[-1]}).")
        return

    print(f"Nota: {n}")

    grau_distraido = fuzz.interp_membership(nota.universe, nota['baixa'].mf, n)
    grau_atento = fuzz.interp_membership(nota.universe, nota['media'].mf, n)
    grau_focado = fuzz.interp_membership(nota.universe, nota['alta'].mf, n)

    print("\nRegras ativas:")
    if grau_distraido > 0:
        print(f" → Regra 1: nota baixa → atenção distraída (grau de ativação: {grau_distraido:.2%})")
    if grau_atento > 0:
        print(f" → Regra 2: nota média → atenção atenta (grau de ativação: {grau_atento:.2%})")
    if grau_focado > 0:
        print(f" → Regra 3: nota alta → atenção focada (grau de ativação: {grau_focado:.2%})")

    
    simulador.input['nota'] = n
    simulador.compute()

    
    atencao_resultado = simulador.output['atencao']
    print(f"\nResultado fuzzy: Atenção = {atencao_resultado:.2f}")

    
    print("\nExibindo gráficos dos conjuntos fuzzy...")
    nota.view(sim=simulador)
    atencao.view(sim=simulador)

regras_ativas_gaussiana()