import streamlit as st

st.title("Alejandro")
st.caption("soy orgullosamente UIS ;P ")
st.caption("amante las matematicas, casado con el arte")

#titulos
st.title("grande") 
st.header("mediano") 
st.subheader("pequeño")

#textos
st.markdown("""
en esto puedes poner cualquier texto
poner un texto en **negrilla**, *italica* o en ***ambos***

enumeraciones:

1.primer item

2.segundo item

3.tercer item

+ 1item
+ 2item
+ 3item



podemos dar color al texto :red[rojo]



""")

# para copiar cosas centradas bonitas
st.latex('mx+b =y')

#elemeto multimedia imagen o video
st.image('https://art3x2.com/storage/posts/65e58fecb5535.webp')
#st.video('')


#encerar un contenido en un marco
with st.container(border=True):
    st.markdown('pepe')
    st.latex('pepito')


#para hacer columnas

c1,c2 =st.columns(2)

with c1:
    st.markdown("primera columna ")


with c2:
    st.markdown("segunda columna")