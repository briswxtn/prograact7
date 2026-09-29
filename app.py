import streamlit as st
st.title("Evaluación de un lote")

st.sidebar.title("Act. Programación")
st.sidebar.write("Universidad Autónoma de Chihuahua - Facultad de Ciencias Químicas - Brissa Aracely Carrasco Iglesias 3°L (395007)")

pH = st.number_input(
  "pH",
  value = 6.5
)

temperatura = st.number_input(
  "Temperatura (°C)",
  value = 23.0
)

if st.button("Evaluar"):
  if pH > 7:
    st.write("Revisar pH")
  elif pH < 6:
    st.write("Revisar pH")
else:
  st.write("pH adecuado")
