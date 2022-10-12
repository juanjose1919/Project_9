import streamlit as st
import numpy as np
import pandas as pd
import pickle as pk


st.sidebar.markdown(f'<h1 style="text-align: center; color:#F7D559;font-size:35px;">{"INTRODUCCIÓN"}</h1>', unsafe_allow_html=True)
st.sidebar.markdown(f'<h1 style="text-align: center; color:#000000;font-size:22px;">{"en este proyecto se analizaron diferentes variables que trataban diferentes características de una población determinada, siendo así datos importantes al momento de realizar una predicción del salario con el modelo Random Forest de regresión, sin embargo, se hizo necesario llevar a cabo tanto una limpieza de los datos como un filtro de las variables, buscando tener en cuenta aquellos datos que mayor influencia tienen sobre la predicción del ingreso como variable objetivo"}</h1>', unsafe_allow_html=True)



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
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6426:"}</h1>', unsafe_allow_html=True)
st.write('Es el tiempo que lleva trabajando en la misma empresa')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6510:"}</h1>', unsafe_allow_html=True)
st.write('Es la variable de ingresos por horas extra del mes pasado. Siendo 1: Si, 2: No, 3: No sabe, no informa')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6590:"}</h1>', unsafe_allow_html=True)
st.write('Indica si el trabajador recibió, además del salario en dinero, alimentos como parte de pago por su trabajo el mes pasado. Siendo 1: Si, 2: No, 3: No sabe, no informa')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6990:"}</h1>', unsafe_allow_html=True)
st.write('Hace referencia a la afiliación del trabajador a una aseguradora de riesgos profesionales. Siendo 1: Si, 2: No, 3: No sabe, no informa')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6430:"}</h1>', unsafe_allow_html=True)
st.write('Indica su posición en el trabajo. Siendo 1: Obrero o empleado de empresa particular, 2: Obrero o empleado del gobierno, 3: Empleado doméstico, 4: Trabajador por cuenta propia, 5: Patrón o empleador, 6: Trabajador familiar sin remuneración, 7: Trabajador sin remuneración en empresas o negocios de otros familiares, 8: Jornalero o peón, 9: otro')
st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6500:"}</h1>', unsafe_allow_html=True)
st.write('Hace referencia a las ganancias del trabajador en el mes pasado antes de descuentos')

