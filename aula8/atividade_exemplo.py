"""
Instalar bibliotecas
!pip install scikit-fuzzy
"""

# Bibliotecas
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temperatura = ctrl.Antecedent(np.arange(0, 151, 1), 'temperatura')
vibracao = ctrl.Antecedent(np.arange(0, 11, 0.1), 'vibracao')
corrente = ctrl.Antecedent(np.arange(0, 51, 1), 'corrente')
fp = ctrl.Antecedent(np.arange(0.0, 1.01, 0.01), 'fator_potencia')
mtbf = ctrl.Antecedent(np.arange(0, 3001, 10), 'mtbf')

risco_falha = ctrl.Consequent(np.arange(0, 101, 1), 'risco_falha')

# Funções de pertinência
temperatura['baixa'] = fuzz.trapmf(temperatura.universe, [0, 0, 40, 60])
temperatura['normal'] = fuzz.trimf(temperatura.universe, [60, 80, 100])
temperatura['alta'] = fuzz.trapmf(temperatura.universe, [90, 110, 150, 150])

vibracao['leve'] = fuzz.trapmf(vibracao.universe, [0, 0, 1.5, 2.8])
vibracao['moderada'] = fuzz.trimf(vibracao.universe, [2.0, 3.5, 4.5])
vibracao['severa'] = fuzz.trapmf(vibracao.universe, [4.0, 6.0, 10, 10])

corrente['baixa'] = fuzz.trapmf(corrente.universe, [0, 0, 15, 21])
corrente['nominal'] = fuzz.trimf(corrente.universe, [20, 30, 33])
corrente['alta'] = fuzz.trapmf(corrente.universe, [31, 35, 50, 50])

fp['ruim'] = fuzz.trapmf(fp.universe, [0.0, 0.0, 0.6, 0.75])
fp['regular'] = fuzz.trimf(fp.universe, [0.7, 0.8, 0.9])
fp['bom'] = fuzz.trapmf(fp.universe, [0.85, 0.9, 1.0, 1.0])

mtbf['curto'] = fuzz.trapmf(mtbf.universe, [0, 0, 300, 500])
mtbf['medio'] = fuzz.trimf(mtbf.universe, [400, 1000, 1500])
mtbf['longo'] = fuzz.trapmf(mtbf.universe, [1200, 1800, 3000, 3000])

risco_falha['baixo'] = fuzz.trapmf(risco_falha.universe, [0, 0, 25, 40])
risco_falha['medio'] = fuzz.trimf(risco_falha.universe, [35, 55, 70])
risco_falha['alto'] = fuzz.trapmf(risco_falha.universe, [65, 80, 100, 100])

rules = [
    ctrl.Rule(temperatura['alta'] | vibracao['severa'] | corrente['alta'], risco_falha['alto']),
    ctrl.Rule(temperatura['normal'] & vibracao['moderada'] & corrente['nominal'], risco_falha['medio']),
    ctrl.Rule(temperatura['baixa'] & vibracao['leve'] & corrente['baixa'] & fp['bom'] & mtbf['longo'], risco_falha['baixo']),
    ctrl.Rule(fp['ruim'] | mtbf['curto'], risco_falha['alto']),
    ctrl.Rule(fp['regular'] & mtbf['medio'], risco_falha['medio']),
    ctrl.Rule(fp['bom'] & mtbf['longo'], risco_falha['baixo'])
]

# Sistema de controle
risco_ctrl = ctrl.ControlSystem(rules)
simulador = ctrl.ControlSystemSimulation(risco_ctrl)

simulador.input['temperatura'] = 85
simulador.input['vibracao'] = 3.5
simulador.input['corrente'] = 30
simulador.input['fator_potencia'] = 0.82
simulador.input['mtbf'] = 1000

simulador.compute()
print(f"Resultado de teste: Risco de Falha = {simulador.output['risco_falha']:.2f}")

# Função de interação
def regras_ativas_motor():
    try:
        # Entradas manuais
        temp = float(input("Temperatura (0 a 150 ºC): "))
        vib = float(input("Vibração (0 a 10 mm/s): "))
        corr = float(input("Corrente (0 a 50 A): "))
        fator_potencia_input = float(input("Fator de potência (0.0 a 1.0): "))
        tempo_mtbf = float(input("MTBF (0 a 3000 h): "))

        # Validação (básica, pode ser expandida)
        if not (0 <= temp <= 150 and 0 <= vib <= 10 and 0 <= corr <= 50 and
                0.0 <= fator_potencia_input <= 1.0 and 0 <= tempo_mtbf <= 3000):
            print("Um ou mais valores estão fora dos limites permitidos.")
            return

        # Mostrar valores informados
        print(f"\nEntradas:")
        print(f"Temperatura: {temp} ºC")
        print(f"Vibração: {vib} mm/s")
        print(f"Corrente: {corr} A")
        print(f"Fator de Potência: {fator_potencia_input}")
        print(f"MTBF: {tempo_mtbf} h")

        # Graus de pertinência
        print("\nGraus de pertinência (ativação dos conjuntos fuzzy):")

        print("→ Temperatura:")
        for termo in temperatura.terms:
            grau = fuzz.interp_membership(temperatura.universe, temperatura[termo].mf, temp)
            if grau > 0:
                print(f"   - {termo}: {grau:.2%}")

        print("→ Vibração:")
        for termo in vibracao.terms:
            grau = fuzz.interp_membership(vibracao.universe, vibracao[termo].mf, vib)
            if grau > 0:
                print(f"   - {termo}: {grau:.2%}")

        print("→ Corrente:")
        for termo in corrente.terms:
            grau = fuzz.interp_membership(corrente.universe, corrente[termo].mf, corr)
            if grau > 0:
                print(f"   - {termo}: {grau:.2%}")

        print("→ Fator de Potência:")
        for termo in fp.terms:
            grau = fuzz.interp_membership(fp.universe, fp[termo].mf, fator_potencia_input)
            if grau > 0:
                print(f"   - {termo}: {grau:.2%}")

        print("→ MTBF:")
        for termo in mtbf.terms:
            grau = fuzz.interp_membership(mtbf.universe, mtbf[termo].mf, tempo_mtbf)
            if grau > 0:
                print(f"   - {termo}: {grau:.2%}")

        # Inserir valores no sistema fuzzy
        simulador.input['temperatura'] = temp
        simulador.input['vibracao'] = vib
        simulador.input['corrente'] = corr
        simulador.input['fator_potencia'] = fator_potencia_input
        simulador.input['mtbf'] = tempo_mtbf

        # Computar o resultado
        simulador.compute()

        # Saída
        resultado = simulador.output['risco_falha']
        print(f"\nResultado fuzzy: Risco de Falha = {resultado:.2f}")

        # Exibição gráfica dos conjuntos fuzzy
        print("\nExibindo gráficos...")
        risco_falha.view(sim=simulador)

    except Exception as e:
        print(f"Erro: {e}")

regras_ativas_motor()