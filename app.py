import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.write("""
        # Bienvenidos
         """)

archivo = pd.ExcelFile("DATOS_2024_SEM_2.xlsx")
# archivo.sheet_names

st.write("Cargando los precios de las casas de boston en el archivo Housing")

housing = archivo.parse("Housing")
st.dataframe(housing.head(n=3))
st.dataframe(housing.tail(n=3))

# Crear el gráfico
fig, ax = plt.subplots()
ax.hist(housing['median_house_value'], bins=30, color='skyblue', edgecolor='black')
ax.set_title('Distribución de los Valores Medianos de las Casas en Boston')
ax.set_xlabel('Valor Mediano de la Casa')
ax.set_ylabel('Frecuencia')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

# Crear el gráfico
fig = px.histogram(housing, x='median_house_value', nbins=30, title='Distribución de los Valores Medianos de las Casas en Boston')

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

# Crear el gráfico KDE
fig, ax = plt.subplots()
sns.kdeplot(housing['median_house_value'], ax=ax, fill=True, color='skyblue')
ax.set_title('Estimación de Densidad del Kernel de los Valores Medianos de las Casas en Boston')
ax.set_xlabel('Valor Mediano de la Casa')
ax.set_ylabel('Densidad')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)