# Instalar biblioteca
'''
Caso utilize o Colab
!pip install scikit-fuzzy 
'''

# Bibliotecas
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. Variáveis fuzzy
temperatura = ctrl.Antecedent(np.arange(0, 51, 1), 'temperatura')
conforto = ctrl.Consequent(np.arange(0, 41, 1), 'conforto')

# 2. Conjuntos fuzzy para temperatura
temperatura['frio'] = fuzz.trimf(temperatura.universe, [0, 15, 25])
temperatura['agradavel'] = fuzz.trimf(temperatura.universe, [15, 25, 35])
temperatura['quente'] = fuzz.trimf(temperatura.universe, [25, 35, 45])

# 3. Conjuntos para conforto
conforto['baixo'] = fuzz.trimf(conforto.universe, [0, 15, 25])
conforto['medio'] = fuzz.trimf(conforto.universe, [25, 35, 45])
conforto['alto'] = fuzz.trimf(conforto.universe, [15, 25, 35])

# 4. Regras fuzzy
regra1 = ctrl.Rule(temperatura['frio'], conforto['baixo'])
regra2 = ctrl.Rule(temperatura['quente'], conforto['medio'])
regra3 = ctrl.Rule(temperatura['agradavel'], conforto['alto'])

# 5. Sistema de controle
sistema = ctrl.ControlSystem([regra1, regra2, regra3])
simulador = ctrl.ControlSystemSimulation(sistema)