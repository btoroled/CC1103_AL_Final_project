# PCA para Reducción de Dimensionalidad en Datos Biomédicos (BRCA-W)

Proyecto de **Análisis de Componentes Principales (PCA)** aplicado a datos biomédicos (dataset BRCA-W / *Wisconsin Diagnostic Breast Cancer*), conectando la teoría de álgebra lineal (matriz de covarianza, valores/vectores propios, SVD) con una implementación práctica en Python.

---

## Integrantes (4)
> Completa con los datos de tu equipo.

| # | Nombre | Rol | Email/GitHub |
|---|--------|-----|--------------|
| 1 | **[Nombre 1]** | Líder del proyecto | [@usuario] / [correo] |
| 2 | **[Nombre 2]** | Experto/a en teoría | [@usuario] / [correo] |
| 3 | **[Nombre 3]** | Analista de resultados | [@usuario] / [correo] |
| 4 | **[Nombre 4]** | Comunicador/a (informe + presentación) | [@usuario] / [correo] |

---

## Objetivos
- Comprender y construir la **matriz de covarianza** y sus propiedades.
- Calcular e interpretar **valores propios** y **vectores propios** en PCA.
- Conectar PCA con **SVD** como enfoque computacional equivalente.
- Analizar **varianza explicada** y decidir cuántos componentes conservar.
- Implementar y visualizar PCA en Python sobre un dataset biomédico.

---

## Dataset
Usamos el dataset BRCA-W (569 observaciones, 30 variables numéricas) con dos clases (benigno/maligno) y aplicamos PCA para proyectar a 2D/3D y analizar separabilidad.

---

## Estructura sugerida del repositorio
```
.
├── codigos/
│   ├── 
├── src/
│   ├──
├── report/
│   ├── 
└── README.md
```

---

## Requisitos
- Python 3.10+ (recomendado)
- Librerías: `numpy`, `pandas`, `scikit-learn`, `matplotlib` (y opcionalmente `seaborn`)

---

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

**`requirements.txt` (ejemplo)**
```txt
numpy
pandas
scikit-learn
matplotlib
seaborn
```

---

## Metodología (pipeline)
1. **Centrado/Estandarización** de datos.
2. Construcción/uso de **S** (matriz de covarianza) y/o **SVD**.
3. Extracción de **cargas (loadings)** y **puntuaciones (scores)**.
4. **Varianza explicada** (individual y acumulada).
5. **Visualización** (2D/3D, scree plot) y conclusiones.

---

## Entregables (checklist)
### Entregable 1 (teórico – resumen)
- Justificación de la condición para soluciones no triviales en el eigenproblema.
- Demostración paso a paso de una igualdad clave asociada a SVD y propiedad usada.
- Propiedades de matrices ortogonales (ortonormalidad, inversa = transpuesta).
- Ejemplo de matriz ortogonal 2×2 (rotación), aplicación a un vector y preservación de norma.
- Demostrar que \(A^T A\) es semidefinida positiva.

### Entregable 2 (teórico + computacional – resumen)
- Teorema espectral (enunciado + relevancia para PCA).
- Interpretación de forma y varianza explicada en PCA con 2 componentes.
- PCA con **3 componentes**: tabla de varianza individual/acumulada + **scree plot**.
- Verificación computacional de ortogonalidad de `pca.components_`.
- Verificación numérica de relación entre valores propios y valores singulares.
- Informe final: resumen, objetivos, metodología, resultados, conclusiones.
