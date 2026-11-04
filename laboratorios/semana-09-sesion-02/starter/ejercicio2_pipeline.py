"""Ejercicio 2: el pipeline completo de viajes_features.csv.

Corre el script con:

    python3 ejercicio2_pipeline.py

Al final se imprime una comprobacion por cada TODO. No la modifiques:
cuando las cinco digan OK, pasa a las preguntas del README.
"""

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

viajes = pd.read_csv("viajes_features.csv")

NUMERICAS = ["distancia_km", "pasajeros"]
YA_LISTAS = ["hora_sin", "hora_cos", "es_fin_de_semana", "es_hora_pico", "es_tarifa_fija"]
CATEGORICAS = ["zona_origen", "zona_destino", "metodo_pago"]

X = viajes[NUMERICAS + YA_LISTAS + CATEGORICAS]
y = viajes["tarifa"]

# TODO 1: separar entrenamiento y prueba.
X_ent, X_prueba, y_ent, y_prueba = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# TODO 2: definir la preparación por tipo de columna.
pipeline_numericas = Pipeline([
    ("imputar", SimpleImputer(strategy="median")),
    ("escalar", StandardScaler()),
])

pipeline_categoricas = Pipeline([
    ("imputar", SimpleImputer(strategy="most_frequent")),
    (
        "codificar",
        OneHotEncoder(
            handle_unknown="ignore",
            sparse_output=False,
        ),
    ),
])

preparacion = ColumnTransformer([
    ("numericas", pipeline_numericas, NUMERICAS),
    ("ya_listas", "passthrough", YA_LISTAS),
    ("categoricas", pipeline_categoricas, CATEGORICAS),
])

# TODO 3: aprender únicamente con entrenamiento.
X_ent_listo = preparacion.fit_transform(X_ent)
X_prueba_listo = preparacion.transform(X_prueba)

print("Columnas después de preparar:", X_ent_listo.shape[1])
print("Forma de entrenamiento:", X_ent_listo.shape)
print("Forma de prueba:", X_prueba_listo.shape)

# TODO 4: consultar las medianas aprendidas.
medianas_aprendidas = (
    preparacion.named_transformers_["numericas"]
    .named_steps["imputar"]
    .statistics_
)

comparacion_medianas = pd.DataFrame(
    {
        "aprendidas": medianas_aprendidas,
        "entrenamiento": X_ent[NUMERICAS].median(),
        "dataset_completo": X[NUMERICAS].median(),
    },
    index=NUMERICAS,
)

print("\nComparación de medianas:")
print(comparacion_medianas)

# TODO 5: transformar un viaje con una zona desconocida.
nuevo = pd.DataFrame([{
    "distancia_km": 9.0,
    "pasajeros": 1,
    "hora_sin": 0.5,
    "hora_cos": -0.866,
    "es_fin_de_semana": 0,
    "es_hora_pico": 1,
    "es_tarifa_fija": 0,
    "zona_origen": "Bronx",
    "zona_destino": "Midtown",
    "metodo_pago": "tarjeta",
}])

nuevo_listo = preparacion.transform(nuevo)
nombres_columnas = preparacion.get_feature_names_out()

columnas_origen = np.array([
    nombre.startswith("categoricas__zona_origen_")
    for nombre in nombres_columnas
])

zona_origen_en_1 = int(
    np.count_nonzero(nuevo_listo[0, columnas_origen] == 1)
)

print("\nColumnas de zona_origen en 1:", zona_origen_en_1)


def comprobar(numero, condicion):
    if condicion:
        print(f"TODO {numero}: OK")
    else:
        print(f"TODO {numero}: revisa")


print()
print("Comprobacion")
comprobar(1, X_ent is not None and len(X_ent) == 2380 and len(X_prueba) == 595)
comprobar(2, isinstance(preparacion, ColumnTransformer) and len(preparacion.transformers) == 3)
comprobar(3, X_ent_listo is not None and X_ent_listo.shape[1] == 25 and X_prueba_listo.shape[0] == 595)
comprobar(4, medianas_aprendidas is not None and X_ent is not None
          and np.allclose(medianas_aprendidas, X_ent[NUMERICAS].median().values))
comprobar(5, zona_origen_en_1 == 0)
