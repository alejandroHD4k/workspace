import streamlit as st

#1 crear paginas 
intro = st.Page("paginas/intro.py", title="introduccion")
ejs = st.Page("paginas/ejercicios.py", title="ejercicios") 
#graficas = st.Page("paginas/graficas.py", tittle="graficas")
#icon="markdown")
#icon=":material/googlefonts defaul= True)

# 2) navigation
pg = st.navigation([intro, ejs])

#3) ejecuta
pg.run()