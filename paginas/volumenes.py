import streamlit as st


st.title("Volumenes")

st.markdown("""

 Se entiende por volumen a una magnitud métrica, euclideana y de tipo escalar, que se puede definir como la extensión de un objeto en sus tres dimensiones, es decir, tomando en cuenta su longitud, ancho y altura. Todos los cuerpos físicos ocupan un espacio que varía según sus proporciones, y la medida de dicho espacio es el volumen.

 Las formulas para hayar el volumen dependen del tipo de solido que sea, estipulando asi una formula distinta par cada tipo de solido.

 """)

st.header("Prismas")

st.markdown("""

El volumen de un prisma es el producto del área de la base (Ab) por la altura del prisma (h). En un prisma recto la altura coincide con una altura lateral, mientras que en un prisma oblicuo no.

""")


with st.container(border=True):
    
 c1,c2 =st.columns(2)
 with c1:
  with st.container(border=True):
    st.markdown('formula del volumen de un prisma:')
    st.latex('V= Ab * h')
    st.markdown('donde **Ab** es el area de la base y **h** es la altura')
 with c2:
    st.image("imagenes/prisma-removebg-preview.png")

st.header("Piramide")


st.markdown("""

El volumen de una pirámide es un tercio del área de la base de la pirámide (Ab) y su altura (h).

""")
with st.container(border=True):
 c1,c2 =st.columns(2)

 with c1:
   with st.container(border=True):
    st.markdown('formula del volumen de una piramide:')
    st.latex('V= 1/3 * Ab * h')
    st.markdown('donde **Ab** es el area de la base y **h** es la altura')
 with c2:
    st.image("imagenes/piramide-removebg-preview.png")


st.header("Tetraedro")

st.markdown("""

El volumen de un tetraedro se calcula a partir de una de sus aristas (a):

""")
with st.container(border=True):

 c1,c2 =st.columns(2)

 with c1:

   with st.container(border=True):
    st.markdown('formula del volumen de un tetraedro:')
    st.latex('V= (√2/12)* a³')
    st.markdown('donde **a** es una de las aristas del tetraedro')

 with c2:

    st.image("imagenes/tetraedro-removebg-preview.png")

st.header("Cubo (hexaedro regular)")

st.markdown("""

El volumen de un cubo (o hexaedro regular) es igual a la longitud de sus aristas al cubo:

""")
with st.container(border=True):

 c1,c2 =st.columns(2)

 with c1:

   with st.container(border=True):
    st.markdown('formula del volumen de un cubo:')
    st.latex('V= a³')
    st.markdown('donde **a** es una de las aristas del cubo')

 with c2:

    st.image("imagenes/cubo-removebg-preview.png")

st.header("Octaedro")

st.markdown("""

El volumen de un octaedro (u octoedro) se calcula mediante la fórmula siguiente:

""")
with st.container(border=True):

 c1,c2 =st.columns(2)

 with c1:

   with st.container(border=True):
    st.markdown('formula del volumen de un octaedro:')
    st.latex('V= 1/3 √2a³')
    st.markdown('donde **a** es la longitud de una de las aristas del octaedro')

 with c2:

    st.image("imagenes/octaedro-removebg-preview.png")

st.header("Dodecaedro")

st.markdown("""

El volumen de un dodecaedro se calcula sabiendo la longitud de la arista, mediante la fórmula siguiente:

""")
with st.container(border=True):

 c1,c2 =st.columns(2)

 with c1:

   with st.container(border=True):
    st.markdown('formula del volumen de un dodecaedro:')
    st.latex('V= 1/4(15+7√5)a³')
    st.markdown('donde **a** es la longitud de una de las aristas del dodecaedro')

 with c2:

    st.image("imagenes/dodecaedro-removebg-preview.png")

st.header("Icosaedro")

st.markdown("""

El volumen de un icosaedro se puede calcular a partir de una de sus aristas, mediante la fórmula siguiente:

""")
with st.container(border=True):

 c1,c2 =st.columns(2)

 with c1:

   with st.container(border=True):
    st.markdown('formula del volumen de un icosaedro:')
    st.latex('V= 5/12(3+√5)a³')
    st.markdown('donde **a** es la longitud de una de las aristas del icosaedro')

 with c2:

    st.image("imagenes/icosaedro-removebg-preview.png")

st.header("Esfera")

st.markdown("""

El volumen de una esfera se calcula en función de su radio (r). Su fórmula es:

""")
with st.container(border=True):

 c1,c2 =st.columns(2)

 with c1:

   with st.container(border=True):
    st.markdown('formula del volumen de una esfera:')
    st.latex('V=4/3 π * r³')
    st.markdown('donde **r** es el radio de la esfera')

 with c2:

    st.image("imagenes/esfera-removebg-preview.png")

st.header("Cilindro")

st.markdown("""

El volumen de un cilindro se calcula mediante la fórmula:

""")
with st.container(border=True):

 c1,c2 =st.columns(2)

 with c1:

   with st.container(border=True):
    st.markdown('formula del volumen de un cilindro:')
    st.latex('V= π * r³ * h')
    st.markdown('donde **r** es el radio del cilindro y **h** es la altura ')

 with c2:

    st.image("imagenes/cilindro-removebg-preview.png")

st.header("Cono")

st.markdown("""

En el caso del cono de base circular, tanto recto como oblicuo, su volumen será

""")
with st.container(border=True):

 c1,c2 =st.columns(2)

 with c1:

   with st.container(border=True):
    st.markdown('formula del volumen de un cono:')
    st.latex('V= (π * r³ * h)/3')
    st.markdown('donde **r** es el radio del cono y **h** es la altura ')

 with c2:

    st.image("imagenes/cono-removebg-preview.png")

st.header("Toro")

st.markdown("""

El volumen del toro se calcula mediante la fórmula:

""")
with st.container(border=True):

 c1,c2 =st.columns(2)

 with c1:

   with st.container(border=True):
    st.markdown('formula del volumen de un toro:')
    st.latex('V= 2π² * R * r² ')
    st.markdown('donde **r** es el radio del circulo menor y **R** el del mayor ')

 with c2:

    st.image("imagenes/toro-removebg-preview.png")

st.markdown("**Fuentes**")

st.markdown("""

https://concepto.de/volumen/#ixzz8trN8Vub9
https://www.universoformulas.com/matematicas/geometria/volumen/

 """)