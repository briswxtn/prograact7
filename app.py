import streamlit as st
st.title("Evaluación de un lote")

pH = st.number_input(
  "pH",
  value = 6.5
)

temperatura =st.number_input(
  "Temperatura (°C)",
  value = 23.0
)

if st.button("Evaluar"):
  pH > 7:
  st.write("Revisar pH")
elif:
  pH < 6:
  st.write("Revisar pH")
else:
  st.write("pH adecuado")
