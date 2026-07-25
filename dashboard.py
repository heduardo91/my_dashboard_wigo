import streamlit as st 
from conexion import cargar_datos
from indicadores import *
from graficos import *

df = cargar_datos() # UTILIZANDO LA FUNCIÓN QUE NOS DEVUELVE EL DATAFRAME (DF)

# CONFIGURACIÓN DE DASHBOARD CON STREAMLIT:
# ----------------------------------------

st.set_page_config(page_title = "Wigo Motors", 
                   layout="wide")      

#FONDO SUAVE
st.markdown("""
<style>

.stApp{
    background-color:#0E1117;
}

</style>
""", unsafe_allow_html=True)

#ENCABEZADO CON COLOR DE FONDO
st.markdown("""
<div style="
background:linear-gradient(90deg,#1565C0,#D9E2EC);
padding:20px;
border-radius:10px;
text-align:center;
color:white;
">
<h1>🚗 WIGO MOTORS S.A.C.</h1>
<h4>Dashboard Comercial</h4>
</div>
""", unsafe_allow_html=True)

#SEPARADOR AZUL
st.markdown("""
<hr style="height:3px;border:#D9E2EC;background:#1E88E5;">
""", unsafe_allow_html=True)

st.sidebar.header("Buscador")
tipo_busqueda = st.sidebar.selectbox("Seleccione tipo de búsqueda", ["Marca", "Asesor comercial", "Sede"])  

df_filtrado = df.copy()     # Haciendo una copia del DataFrame 


# FILTRO POR MARCA:

if tipo_busqueda == "Marca":
    valor = st.sidebar.selectbox("Seleccionar marca", df["marca"].unique()) # Mostrar las marcas disponibles y sin repetir
    df_filtrado = df[df["marca"] == valor]                                   # Filtrar búsqueda por marca  
    
elif tipo_busqueda == "Asesor comercial":
    valor = st.sidebar.selectbox("Seleccionar asesor", df["asesor_comercial"].unique()) # Mostrar las marcas disponibles y sin repetir
    df_filtrado = df[df["asesor_comercial"] == valor]                                   # Filtrar búsqueda por marca  
    
elif tipo_busqueda == "Sede":
    valor = st.sidebar.selectbox("Seleccionar sede", df["tienda"].unique()) # Mostrar las marcas disponibles y sin repetir
    df_filtrado = df[df["tienda"] == valor]                                   # Filtrar búsqueda por marca  
    

# MOSTRAR RESULTADOS (TABLA):

st.success(f"Registros encontrados: {len(df_filtrado)}")        # Mostrar la cantidad de filas encontradas (color verde)
st.dataframe(df_filtrado)


# INDICADORES GENERALES: 
st.markdown("""
<div style="
background:#0F4C81;
padding:8px;
border-radius:6px;
color:#D9E2EC;
font-size:22px;
font-weight:bold;">
📊 Indicadores
</div>
""", unsafe_allow_html=True)


#INDICADORES EN TARJETAS
st.markdown("""
<style>

div[data-testid="stMetric"]{
    background-color:#1f2937;
    border:1px solid #3b82f6;
    padding:15px;
    border-radius:12px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.3);
}

div[data-testid="stMetricLabel"]{
    font-size:18px;
    font-weight:bold;
}

div[data-testid="stMetricValue"]{
    color:#4FC3F7;
    font-size:30px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)        

c1.metric("Precio Total", f"S/{precio_total(df_filtrado):,.2f}")          
c2.metric("Unidades vendidas", f"{unidades_vendidas(df_filtrado)}")                
c3.metric("Precio promedio", f"S/{precio_promedio(df_filtrado):,.2f}")     
c4.metric("Operaciones", operaciones(df_filtrado))                                      



c5, c6, c7, c8 = st.columns(4)  

c5.metric("Precio más alto", f"S/{precio_maximo(df_filtrado):,.2f}")
c6.metric("Precio más bajo", f"S/{precio_minimo(df_filtrado):,.2f}")


# GRÁFICOS - DASHBOARD 
st.markdown("""
<div style="
background:#1565C0;
padding:8px;
border-radius:6px;
color:white;
font-size:22px;
font-weight:bold;">
📈 Gráficos
</div>
""", unsafe_allow_html=True)
st.markdown("")


g1, g2 = st.columns(2)

with g1:
    st.plotly_chart(grafico_ventas(df_filtrado),
                    use_container_width=True)

with g2:
    st.plotly_chart(grafico_promedio(df_filtrado),
                    use_container_width=True)
