import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("./starter/figuras_smeana8", exist_ok=True)

data = pd.read_csv("laboratorios/semana-09-sesion-01/starter/viajes_taxi.csv")

print("Analisis exploratorio descriptivo")

data.info()

print(data.dtypes)
print(data.isna().sum())
print(data.duplicated().sum())

print(data.describe())

# Histograma
plt.figure()
plt.hist(data['tarifa'], bins =50)
plt. title('Distribución de la tarifa')
plt. xlabel('USD')
plt.ylabel('Nmero de viajes')
plt.savefig('./starter/figuras/hist_tarifa.png')
plt.close()

# Box Plot
plt.figure()
plt.boxplot(data['tarifa'])
plt. title('Boxplot de la tarifa')
plt.savefig('./starter/figuras/boxplot_tarifa.png')
plt.close()

#Extracción de valores atipicos

q1 = data['tarifa'].quantile(0.25)
q3 = data['tarifa'].quantile(0.75)

iqr = q3 - q1

limite_superior = q3 + 1.5 * iqr
limite_inferior = q1 - 1.5 * iqr

atipicos = data.query(f'tarifa < {limite_inferior} or tarifa > {limite_superior}')
sin_atipicos = data.query(f'tarifa >= {limite_inferior} and tarifa <= {limite_superior}')

print(atipicos)


# Scatter atipicos
plt.figure()
plt.scatter(data['tarifa'], data['distancia_km'])
plt. title('Disperción de tarifa vs distancia_km')
plt.savefig('./starter/figuras/dispersion_tarifa.png')
plt.close()

# Scatter sin atipicos
plt.figure()
plt.scatter(sin_atipicos['tarifa'], sin_atipicos['distancia_km'])
plt. title('Disperción de tarifa vs distancia_km')
plt.savefig('./starter/figuras/dispersion_sin_atipicos.png')
plt.close()

# print(data.corr())


