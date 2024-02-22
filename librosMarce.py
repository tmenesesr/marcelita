import streamlit as st
import pandas as pd
import openpyxl

st.set_page_config(layout="wide")
libros = pd.read_excel("miBiblioteca.xlsx")
st.title("Libros de Marcela Vaga")
st.subheader("La más linda")
st.write("")
st.write("")
st.write(libros)
