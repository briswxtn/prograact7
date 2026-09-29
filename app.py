import streamlit as st
st.title("Evaluación de un lote")

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
    if temperatura > 25:
      st.write("Revisar temperatura")
    elif temperatura < 20:
      st.write("Revisar temperatura")
    else:
      st.write("Lote aceptable")
  elif pH < 6:
    st.write("Revisar pH")
else:
  st.write("pH adecuado")
