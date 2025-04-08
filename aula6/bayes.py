# B1 - Hospital
## Manual
# Probabilidades iniciais
p_doenca = 0.01
p_n_doenca = 1- p_doenca

# Probabilidade condicional do teste
p_teste_positivo_doenca = 0.95
p_teste_positivo_n_doenca  = 1- p_teste_positivo_doenca

# Probabilidade total do teste
p_teste_positivo = ((p_teste_positivo_doenca * p_doenca) +
                     (p_teste_positivo_n_doenca * p_n_doenca))

# Probabilidade final
p_doenca_teste_positivo = ((p_teste_positivo_doenca *p_doenca) /
                           p_teste_positivo)

# Impressão formatada
tabela = [
    ("P(Doença)", p_doenca),
    ("P(Não Doença)", p_n_doenca),
    ("P(Teste Positivo | Doença)", p_teste_positivo_doenca),
    ("P(Teste Positivo | Não Doença)", p_teste_positivo_n_doenca),
    ("P(Teste Positivo)", p_teste_positivo),
    ("P(Doença | Teste Positivo)", p_doenca_teste_positivo)
]

print(f"{'Evento':<35} Probabilidade")
print("-" * 50)
for evento, prob in tabela:
    print(f"{evento:<35} {prob*100:.2f}%")

"""## Classificador"""

# Biblioteca
import numpy as np

# Probabilidades iniciais
p_doenca = 0.01
p_n_doenca = 1 - p_doenca

# Probabilidade condicional do teste
p_teste_positivo_doenca = 0.95
p_teste_positivo_nao_doenca = 0.05

# Probabilidade total do teste
p_teste_positivo = (p_teste_positivo_doenca * p_doenca) + (p_teste_positivo_nao_doenca * p_n_doenca)

# Probabilidade final pelo Teorema de Bayes
p_doenca_dado_teste_positivo = (p_teste_positivo_doenca * p_doenca) / p_teste_positivo

# Simulação de pacientes testados
num_pacientes = 1000
resultados_teste = np.random.choice(["positivo", "negativo"], size=num_pacientes,
                                    p=[p_teste_positivo, 1 - p_teste_positivo])

# Classificação com base na probabilidade de ter a doença
limiar = p_doenca_dado_teste_positivo
classificacoes = ["Doente" if np.random.rand() < limiar else "Não Doente" for _ in resultados_teste]

# Exibir os resultados de maneira organizada
print("=" * 60)
print(f"{'Probabilidade de ter a doença dado teste positivo:':<45} {p_doenca_dado_teste_positivo:.2%}")
print("=" * 60)
print(f"{'Total de Pacientes':<50} {num_pacientes}")
print(f"{'Doentes classificados':<50} {classificacoes.count('Doente')}")
print(f"{'Não Doentes classificados':<50} {classificacoes.count('Não Doente')}")
print("=" * 60)

"""# Smurf"""

# Biblioteca
import numpy as np

# Probabilidades iniciais
p_smurf = 0.05
p_normal = 0.95

# Probabilidades condicionais
p_excepcional_dado_smurf = 0.85
p_excepcional_dado_normal = 0.20

p_headshot_alto_dado_smurf = 0.70
p_headshot_alto_dado_normal = 0.15

# ===== Probabilidade total de desempenho excepcional =====
p_excepcional = (
    p_excepcional_dado_smurf * p_smurf +
    p_excepcional_dado_normal * p_normal
)

# ===== Probabilidade de ser smurf dado desempenho excepcional =====
p_smurf_dado_excepcional = (
    p_excepcional_dado_smurf * p_smurf
) / p_excepcional

# ===== Complemento: probabilidade de ser normal dado desempenho excepcional =====
p_normal_dado_excepcional = 1 - p_smurf_dado_excepcional

# ===== Aplicação da Regra de Bayes para o caso do alto headshot =====
p_smurf_dado_excepcional_headshot = (
    p_headshot_alto_dado_smurf * p_smurf_dado_excepcional
) / (
    p_headshot_alto_dado_smurf * p_smurf_dado_excepcional +
    p_headshot_alto_dado_normal * p_normal_dado_excepcional
)

# Impressão formatada dos resultados
print("="*60)
print(f"{'P(desempenho excepcional)':<45} {p_excepcional*100:.2f}%")
print(f"{'P(smurf | desempenho excepcional)':<45} {p_smurf_dado_excepcional*100:.2f}%")
print(f"{'P(smurf | desempenho excepcional + headshot alto)':<45} {p_smurf_dado_excepcional_headshot*100:.2f}%")
print("="*60)

# Número de jogadores a serem classificados
num_jogadores = 1000

# Simulação da classificação dos jogadores
classificacoes = ["Smurf" if np.random.rand() < p_smurf_dado_excepcional_headshot else "Normal"
                  for _ in range(num_jogadores)]

# Contagem dos resultados
num_smurfs = classificacoes.count("Smurf")
num_normais = classificacoes.count("Normal")

# Impressão dos resultados
print("="*60)
print(f"{'Total de Jogadores':<45} {num_jogadores}")
print(f"{'Classificados como Smurf':<45} {num_smurfs}")
print(f"{'Classificados como Normal':<45} {num_normais}")
print("="*60)