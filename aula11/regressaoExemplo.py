# Ex.2 - Regressão (MLP)"""

# Bibliotecas
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. Carregar dados
data = fetch_california_housing()
X, y = data.data, data.target

# 2. Dividir em treino e teste (20% para teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)

# 3. Normalizar dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. MLP com duas camadas ocultas
mlp_reg = MLPRegressor(hidden_layer_sizes=(50, 20), # duas camadas ocultas (50 neurônios, 20 neurônios)
                       activation='relu',
                       max_iter=5000,
                       random_state=42)

# 5. Treinar o modelo
mlp_reg.fit(X_train_scaled, y_train)

# 6. Fazer previsões no conjunto de teste
y_pred = mlp_reg.predict(X_test_scaled)

# 7. Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.4f}")
print(f"R2: {r2:.4f}")