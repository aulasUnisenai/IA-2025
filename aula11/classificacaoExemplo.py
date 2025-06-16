# Ex.1 - Classificação simples (Perceptron x MLP)

# Bibliotecas
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score

# Carregar base Iris
iris = load_iris()
X, y = iris.data, iris.target
class_names = iris.target_names

# Treino e teste (30% para teste)
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=42)

# Normalizar dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modelos
modelos = {
    "Perceptron": Perceptron(max_iter=5000, random_state=42),
    "MLP": MLPClassifier(hidden_layer_sizes=(10,), # uma camada (10 neurônios)
                         activation='relu' ,
                         max_iter=5000, random_state=42)
}

# Avaliação - conjunto de teste
for nome, modelo in modelos.items():
    modelo.fit(X_train_scaled, y_train)
    y_pred = modelo.predict(X_test_scaled)
    print(f"\n=== {nome} ===")
    print("Acurácia:", round(accuracy_score(y_test, y_pred),2))
    print(classification_report(y_test, y_pred,
                                digits=2,
                                target_names=class_names))