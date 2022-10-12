import streamlit as st
import numpy as np
import pandas as pd
import pickle as pk


st.sidebar.markdown(f'<h1 style="text-align: center; color:#F7D559;font-size:35px;">{"INTRODUCCIÓN"}</h1>', unsafe_allow_html=True)
st.sidebar.markdown(f'<h1 style="text-align: center; color:#000000;font-size:22px;">{"En este proyecto se analizaron diferentes variables que trataban diferentes características de una población determinada, siendo así datos importantes al momento de realizar una predicción del salario con el modelo Random Forest de regresión, sin embargo, se hizo necesario llevar a cabo tanto una limpieza de los datos como un filtro de las variables, buscando tener en cuenta aquellos datos que mayor influencia tienen sobre la predicción del ingreso como variable objetivo"}</h1>', unsafe_allow_html=True)



st.sidebar.markdown(f'<h1 style="text-align: center ; color:#F4D03F ;font-size:35px;">{"AUTORES:"}</h1>', unsafe_allow_html=True)

st.sidebar.markdown(f'<h1 style="text-align: center ; color:#000000 ;font-size:22px;">{"Valeria Mendez"}</h1>', unsafe_allow_html=True)
st.sidebar.markdown(f'<h1 style="text-align: center ; color:#000000 ;font-size:22px;">{"Gerardo Pardo"}</h1>', unsafe_allow_html=True)
st.sidebar.markdown(f'<h1 style="text-align: center ; color:#000000 ;font-size:22px;">{"Juan Bohórquez"}</h1>', unsafe_allow_html=True)



st.sidebar.markdown(f'<h1 style="text-align: center; color:#F4D03F ;font-size:30px;">{"FACULDAD DE ECONOMÍA"}</h1>', unsafe_allow_html=True)



st.markdown(f'<h1 style="color:#0E6655  ;font-size:50px;">{"Proyecto 9"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#000000  ;font-size:25px;">{"En este proyecto se analizará el ingreso de los trabajadores mediante el modelo Random Forest, logrando así obtener un modelo que logre predecir el salario por medio de las siguientes variables:"}</h1>', unsafe_allow_html=True)

st.markdown(f'<h1 style="color:#0E6655  ;font-size:35px;">{"Descripción sucinta de las variables"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"Variable dependiente: INGLABO:"}</h1>', unsafe_allow_html=True)
st.write('Constituye los ingresos laborales')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6100:"}</h1>', unsafe_allow_html=True)
st.write('hace referencia a cuál de los regímenes de seguridad social en salud está afiliado: 1. Contributivo (EPS), 2. Especial (Fuerzas Armadas, Ecopetrol, universidades públicas), 3. Subsidiado (EPS-S) 4. No sabe, no informa')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"ESC:"}</h1>', unsafe_allow_html=True)
st.write('Equivale a los años de ecolaridad')

st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6120:"}</h1>', unsafe_allow_html=True)
st.write('¿cuánto paga o cuánto le descuentan mensualmente por la vivienda?')

st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6170:"}</h1>', unsafe_allow_html=True)
st.write('¿Asiste a la escuela, colegio o universidad?')

st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6040:"}</h1>', unsafe_allow_html=True)
st.write('Que edad tiene')

