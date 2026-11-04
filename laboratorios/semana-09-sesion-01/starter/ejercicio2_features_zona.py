"""Ejercicio 2: zona, codificacion y disponibilidad en viajes_taxi.csv.

Corre el script con:

    python3 ejercicio2_features_zona.py

Al final se imprime una comprobacion por cada TODO. No la modifiques:
cuando las cuatro digan OK, pasa a las preguntas del README.
"""

import pandas as pd

viajes = pd.read_csv("viajes_taxi.csv")
viajes = viajes[(viajes["tarifa"] != 999.99) & (viajes["duracion_min"] >= 0)].copy()

ZONAS_MANHATTAN = ["Midtown", "Upper East Side", "Upper West Side", "Lower Manhattan", "Harlem"]

# Guardar las columnas originales antes de agregar características.
columnas_originales = viajes.columns.tolist()

# TODO 1: identificar viajes entre JFK y Manhattan, en ambos sentidos.
desde_jfk = (
    viajes["zona_origen"].eq("JFK Airport")
    & viajes["zona_destino"].isin(ZONAS_MANHATTAN)
)

hacia_jfk = (
    viajes["zona_origen"].isin(ZONAS_MANHATTAN)
    & viajes["zona_destino"].eq("JFK Airport")
)

viajes["es_tarifa_fija"] = (desde_jfk | hacia_jfk).astype(int)

tarifas_fijas = viajes.loc[viajes["es_tarifa_fija"].eq(1), "tarifa"]

print("Viajes con tarifa fija:", len(tarifas_fijas))
print("Tarifa mínima:", tarifas_fijas.min())
print("Tarifa máxima:", tarifas_fijas.max())

# TODO 2: codificación one-hot de la zona de origen.
codificado = pd.get_dummies(
    viajes,
    columns=["zona_origen"],
    prefix="origen",
    dtype=int,
)

columnas_nuevas = [
    columna
    for columna in codificado.columns
    if columna.startswith("origen_")
]

print("\nColumnas one-hot:")
print(columnas_nuevas)

# TODO 3: asignar un entero por zona, en orden alfabético.
zonas_ordenadas = sorted(viajes["zona_origen"].dropna().unique())

mapa_zonas = {
    zona: numero
    for numero, zona in enumerate(zonas_ordenadas)
}

viajes["origen_ordinal"] = (
    viajes["zona_origen"].map(mapa_zonas).astype("Int64")
)

print("\nCodificación ordinal:")
print(mapa_zonas)

# TODO 4: disponibilidad al solicitar el taxi.
# Supuestos: se conocen origen, destino, distancia estimada,
# pasajeros y el método de pago seleccionado.
columnas_disponibles = {
    "id_viaje",
    "fecha_hora_inicio",
    "zona_origen",
    "zona_destino",
    "distancia_km",
    "pasajeros",
    "metodo_pago",
}

disponible_al_pedir = {
    columna: columna in columnas_disponibles
    for columna in columnas_originales
}

print("\nDisponibilidad al pedir el taxi:")
for columna, disponible in disponible_al_pedir.items():
    print(f"{columna}: {disponible}")


def comprobar(numero, condicion):
    if condicion:
        print(f"TODO {numero}: OK")
    else:
        print(f"TODO {numero}: revisa")


print()
print("Comprobacion")
comprobar(1, "es_tarifa_fija" in viajes.columns and viajes["es_tarifa_fija"].sum() == 300)
comprobar(2, codificado is not None
          and len([columna for columna in codificado.columns if columna.startswith("origen_")]) == 8)
comprobar(3, "origen_ordinal" in viajes.columns
          and viajes.loc[viajes["zona_origen"] == "Brooklyn", "origen_ordinal"].iloc[0] == 0
          and viajes["origen_ordinal"].max() == 7)
comprobar(4, disponible_al_pedir is not None
          and disponible_al_pedir.get("duracion_min") is False
          and disponible_al_pedir.get("propina") is False
          and disponible_al_pedir.get("distancia_km") is True)
