import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)  
y = pd.Series(data.target, name="clase")               

print("X shape:", X.shape)
print("y shape:", y.shape)
print("Clases (conteo):\n", y.value_counts())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  

print("\nX_scaled shape:", X_scaled.shape)


pca2 = PCA(n_components=2)
X_pca2 = pca2.fit_transform(X_scaled)

var2 = pca2.explained_variance_ratio_
cum2 = np.cumsum(var2)

print("\n--- PCA (2 componentes) ---")
print("X_pca2 shape:", X_pca2.shape)
print("Varianza explicada (PC1, PC2):", var2)
print("Varianza acumulada:", cum2)

# Scatter PC1 vs PC2 (clase 0/1)
plt.figure(figsize=(7, 5))
plt.scatter(X_pca2[y == 0, 0], X_pca2[y == 0, 1], label="Clase 0", alpha=0.7)
plt.scatter(X_pca2[y == 1, 0], X_pca2[y == 1, 1], label="Clase 1", alpha=0.7)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA (2 componentes) - Scatter PC1 vs PC2")
plt.legend()
plt.grid(True)
plt.show()


pca3 = PCA(n_components=3)
X_pca3 = pca3.fit_transform(X_scaled)

var3 = pca3.explained_variance_ratio_
cum3 = np.cumsum(var3)

tabla3 = pd.DataFrame({
    "Componente": ["PC1", "PC2", "PC3"],
    "Varianza_explicada": var3,
    "Varianza_acumulada": cum3
})

print("\n--- PCA (3 componentes) ---")
print("X_pca3 shape:", X_pca3.shape)
print("\nTabla varianza (3 comps):")
print(tabla3)

# Scree plot (3 componentes)
plt.figure(figsize=(7, 4))
plt.plot([1, 2, 3], var3, marker="o")
plt.xticks([1, 2, 3], ["PC1", "PC2", "PC3"])
plt.xlabel("Componente")
plt.ylabel("Varianza explicada")
plt.title("Scree plot (3 componentes)")
plt.grid(True)
plt.show()


C = pca3.components_   
M = C @ C.T           
I = np.eye(3)

np.set_printoptions(precision=10, suppress=True)

print("\n--- Ortogonalidad de components_ ---")
print("C shape:", C.shape)
print("C @ C.T =\n", M)
print("¿Es ~ identidad?:", np.allclose(M, I, atol=1e-10))
print("Error máximo |M - I|:", np.max(np.abs(M - I)))

n = X_scaled.shape[0]

S = np.cov(X_scaled.T)  

eigvals = np.linalg.eigh(S)[0]   
eigvals = eigvals[::-1]          

sing_vals = np.linalg.svd(X_scaled, compute_uv=False)  
