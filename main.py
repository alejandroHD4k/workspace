import streamlit as st

#1 crear paginas 
intro = st.Page("paginas/intro.py", title="Introdución", icon=":material/home:")
areas = st.Page ("paginas/areas.py", title="Areas", icon=":material/check_box_outline_blank:") 
volumenes = st.Page("paginas/volumenes.py", title="Volumenes", icon=":material/deployed_code:") 
es = st.Page("paginas/es.py", title="Evaluacion", icon=":material/bar_chart:")
pr = st.Page("paginas/presentacion.py", title="creador", icon=":material/person:")
#graficas = st.Page("paginas/graficas.py", tittle="graficas")
#icon=":material/googlefonts defaul= True)

# 2) navigation
pg = st.navigation([intro, areas, volumenes, es, pr])

#3) ejecuta
pg.run()