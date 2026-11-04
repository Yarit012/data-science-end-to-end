"""Ejercicio 2: relaciones entre variables de viajes_taxi.csv.

Corre el script con:

    python3 ejercicio2_relaciones.py

Al final se imprime una comprobacion por cada TODO. No la modifiques:
cuando las cinco digan OK, pasa a los hallazgos del README.
"""

import os

import matplotlib.pyplot as plt
import pandas as pd

os.makedirs("figuras", exist_ok=True)
viajes = pd.read_csv("viajes_taxi.csv")

# TODO 1: quitar únicamente los errores confirmados.
limpios = viajes.loc[
    (viajes["tarifa"] != 999.99)
    & ~(viajes["duracion_min"] < 0)
].copy()

print("Filas después de quitar errores:", len(limpios))

# TODO 2: gráfico de distancia frente a tarifa.
plt.figure(figsize=(9, 6))
plt.scatter(
    limpios["distancia_km"],
    limpios["tarifa"],
    alpha=0.4,
    s=15,
)
plt.xlabel("Distancia (km)")
plt.ylabel("Tarifa (USD)")
plt.title("Distancia frente a tarifa")
plt.grid(alpha=0.2)
plt.tight_layout()
plt.savefig("figuras/distancia_vs_tarifa.png", dpi=150)
plt.show()
plt.close()

# Filtro exploratorio: revisar si los viajes con tarifa 70
# forman un patrón distinto de la tendencia general.
tarifa_fija = limpios.loc[limpios["tarifa"] == 70]

print("Viajes con tarifa de 70 USD:", len(tarifa_fija))
print(tarifa_fija[["distancia_km", "tarifa"]].head(10))

# TODO 3: resumen de propinas por método de pago.
resumen_propina = (
    limpios.groupby("metodo_pago")
    .agg(
        propina_promedio=("propina", "mean"),
        cantidad_viajes=("metodo_pago", "size"),
        viajes_propina_cero=("propina", lambda valores: valores.eq(0).sum()),
    )
)

print("\nPropinas por método de pago:")
print(resumen_propina)

# TODO 4: correlación de cada variable con la tarifa.
columnas = [
    "distancia_km",
    "duracion_min",
    "pasajeros",
    "propina",
    "tarifa",
]

correlaciones = (
    limpios[columnas]
    .corr(method="pearson")["tarifa"]
    .drop("tarifa")
)

print("\nCorrelaciones con la tarifa:")
print(correlaciones)

# TODO 5: distinguir pasajeros ausentes de pasajeros iguales a cero.
pasajeros_vacios = int(limpios["pasajeros"].isna().sum())
pasajeros_cero = int(limpios["pasajeros"].eq(0).sum())

print("\nViajes con pasajeros vacío:", pasajeros_vacios)
print("Viajes con pasajeros igual a 0:", pasajeros_cero)


def comprobar(numero, condicion):
    if condicion:
        print(f"TODO {numero}: OK")
    else:
        print(f"TODO {numero}: revisa")


if isinstance(correlaciones, pd.DataFrame):
    correlaciones = correlaciones["tarifa"]

print()
print("Comprobacion")
comprobar(1, len(limpios) == 2975)
comprobar(2, os.path.exists("figuras/distancia_vs_tarifa.png"))
comprobar(3, resumen_propina is not None and len(resumen_propina) == 2)
comprobar(4, correlaciones is not None and round(float(correlaciones["distancia_km"]), 2) == 0.96)
comprobar(5, pasajeros_vacios == 119 and pasajeros_cero == 19)
