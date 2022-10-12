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

st.image('./descarga.png')
st.image('./beeswarm.png')

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

P6040 = st.slider('¿Cuantos años tiene?')
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
P6050 = st.selectbox('¿Cuál es el parentesco de con el jefe o jefa del hogar?', ('1. Jefe(a) del hogar', '2. Pareja, esposo(a), cónyuge, compañero(a)', '3. Hijo(a), hijastro(a)', '4. Nieto(a)', '5. Otro pariente', '6. Empleado(a) del servicio doméstico y sus parientes', '7. Pensionista', '8. Trabajador', '9. Otro no pariente'))



if P6585S4 == '1. SI':
    P6585S4 = 1
if P6585S4 == '2. NO':
    P6585S4 = 2
if P6585S4 == '3. NO SABE/NO RESPONDE':
    P6585S4 = 3


if P6100 == '1: Obrero o empleado de empresa particular':
    P6100 = 1
if P6100 == '2: Obrero o empleado del gobierno':
    P6100 = 2
if P6100 == '3: Empleado doméstico':
    P6100 = 3
if P6100 == '4: Trabajador por cuenta propia':
    P6100 = 4
if P6100 == '5: Patrón o empleador':
    P6100 = 5
if P6100 == '6: Trabajador familiar sin remuneración':
    P6100 = 6
if P6100 == '7: Trabajador sin remuneración en empresas o negocios de otros familiares':
    P6100 = 7
if P6100 == '8: Jornalero o peón':
    P6100 = 8
if P6100 == '9: otro':
    P6100 = 9

    
if P6050 == '1. SI':
    P6050 = 1
if P6050 == '2. NO':
    P6050 = 2

if P6050 == '1. Jefe(a) del hogar':
    P6050 = 1
if P6050 == '2. Pareja, esposo(a), cónyuge, compañero(a)':
    P6050 = 2
if P6050 == '3. Hijo(a), hijastro(a)':
    P6050 = 3
if P6050 == '4. Nieto(a)':
    P6050 = 4
if P6050 == '5. Otro pariente':
    P6050 = 5
if P6050 == '6. Empleado(a) del servicio doméstico y sus parientes':
    P6050 = 6
if P6050 == '7. Pensionista':
    P6050 = 7
if P6050 == '8. Trabajador':
    P6050 = 8
if P6050 == '9. Otro no pariente':
    P6050 = 9
    

Archivo_2 = open('Archivo_modelo_def','rb')
lista_1 = pk.load(Archivo_2)
print(lista_1)
    
if P6120 and  P6430 and P6100 and P6050:
    a = [P6120, ESC, P6430, P6800, P6040, P6100, P6585S4]
    prediccion = lista_1.predict(a).reshape(1,7)
    st.write('su salario será de', prediccion[0]) 


