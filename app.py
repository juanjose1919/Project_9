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

st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6120:"}</h1>', unsafe_allow_html=True)
P6120 = st.number_input('Muestra cuánto paga o cuánto le descuentan mensualmente a un afiliado, cotizante o beneficiario de alguna entidad de seguridad social en salud')
st.write('El pago o descuento es $', P6120, 'de pesos colombianos')
st.write('')

st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"ESC:"}</h1>', unsafe_allow_html=True)
st.write('')
ESC = st.slider('¿Cuantos años tiene de escolaridad? Escriba 0 si es menor de 1', 0, 70, 0)
st.write("Usted trabaja", ESC, 'meses en la misma empresa')

st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6430:"}</h1>', unsafe_allow_html=True)
P6430 = st.selectbox(
    'Indique cual es su posición en el puesto de trabajo actual',
    ('1: Obrero o empleado de empresa particular', '2: Obrero o empleado del gobierno', '3: Empleado doméstico', '4: Trabajador por cuenta propia', '5: Patrón o empleador', '6: Trabajador familiar sin remuneración', '7: Trabajador sin remuneración en empresas o negocios de otros familiares', '8: Jornalero o peón', '9: otro'))

P6800 = st.slider('¿Número de horas trabajadas a la semana? Escriba 0 si es menor de 1', 0, 100, 0)
st.write("Usted trabaja", P6800, 'meses en la misma empresa')

P6040 = st.slider('¿Cuantos años tiene? 18, 100, 0')
st.write("Usted trabaja", P6040, 'meses en la misma empresa')

st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6100:"}</h1>', unsafe_allow_html=True)
P6100 = st.selectbox(
    '¿Cuenta con un Regímen de seguridad social en salud? ¿Cual?',
    (' 1. Contributivo (EPS)', '2. Especial (Fuerzas Armadas, Ecopetrol, universidades públicas)', '3. Subsidiado (EPS-S', '4. No sabe, no informa'))
st.write('Recibió ingresos por horas extra el mes pasado?', P6100)

st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6585S4::"}</h1>', unsafe_allow_html=True)
P6585S4 = st.selectbox(
    '¿Recibió subsidio educativo el mes pasado? ¿Cual?',
     ('1. SI', '2. NO', '3. NO SABE/NO RESPONDE'))
                  

st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6426:"}</h1>', unsafe_allow_html=True)                 
P6426 = st.slider('Tiempo que lleva trabajando en esta empresa, negocio, industria, oficina, firma o finca de manera continua en meses', 0, 500, 0)
st.write("Usted trabaja", P6426, 'meses en la misma empresa')


st.markdown(f'<h1 style="color:#9A7D0A  ;font-size:25px;">{"P6050:"}</h1>', unsafe_allow_html=True)
P6050 = st.selectbox('¿Es jefe o jefa de hogar?', ('1. SI', '2. NO'))

if horas_add == '1. SI':
    horas_add = 1
if horas_add == '2. NO':
    horas_add = 2
if horas_add == '3. NO SABE/NO RESPONDE':
    horas_add = 3

if subsidio == '1. SI':
    subsidio = 1
if subsidio == '2. NO':
    subsidio = 2
if subsidio == '3. NO SABE/NO RESPONDE':
    subsidio = 3

if afiliación_aseg == '1. SI':
    afiliación_aseg = 1
if afiliación_aseg == '2. NO':
    afiliación_aseg = 2
if afiliación_aseg == '3. NO SABE/NO RESPONDE':
    afiliación_aseg = 3


if posición_trab == '1: Obrero o empleado de empresa particular':
    posición_trab = 1
if posición_trab == '2: Obrero o empleado del gobierno':
    posición_trab = 2
if posición_trab == '3: Empleado doméstico':
    posición_trab = 3
if posición_trab == '4: Trabajador por cuenta propia':
    posición_trab = 4
if posición_trab == '5: Patrón o empleador':
    posición_trab = 5
if posición_trab == '6: Trabajador familiar sin remuneración':
    posición_trab = 6
if posición_trab == '7: Trabajador sin remuneración en empresas o negocios de otros familiares':
    posición_trab = 7
if posición_trab == '8: Jornalero o peón':
    posición_trab = 8
if posición_trab == '9: otro':
    posición_trab = 9


