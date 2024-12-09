import streamlit as st


st.title("Áreas")

st.markdown("""  

Se utiliza el área para medir el espacio de la superficie de la figura que se encuentra delimitado por su contorno.

El área de un polígono dependerá del tipo de polígono que se esté estudiando, de la cantidad de lados que tenga y de las características que lo definan. Aunque de manera general, los cálculos siempre involucran la base y la altura del polígono al cual se le desea hallar el área.

""")

st.header("Rectángulos")

st.markdown("""  

Para hallar el área de un rectángulo, se considera la medida de la base y la altura.

Sin embargo, como el rectángulo es un paralelogramo con lados paralelos e iguales dos a dos, la base coincide con uno de los lados y la altura corresponde al otro lado de diferente medida.

Por esto se define el área de un rectángulo, como el producto de la medida sus lados diferentes, es decir; el lado de mayor longitud por el lado de menor longitud.

""")
with st.container(border=True):
 c1,c2 =st.columns(2)

 with c1:
  with st.container(border=True):
    st.markdown('formula del área de un rectangulo:')
    st.latex('A= b * a')
    st.markdown('donde **b** es la base y **a** es la altura')
 with c2:
    st.image("imagenes/rectangulo-removebg-preview.png")

st.header("Cuadrados")

st.markdown(""" 

El área del cuadrado es el producto de la base por la altura del cuadrado. Ahora bien, como todos los lados del cuadrado son de igual medida, el área es igual a uno de sus lados al cuadrado.

""")
with st.container(border=True):
 c1,c2 =st.columns(2)

 with c1:
  with st.container(border=True):
    st.markdown('formula del área de un cuadrado:')
    st.latex('A= x²')
    st.markdown('donde **x** es un lado del cuadrado')
 with c2:
    st.image("imagenes/cuadrado-removebg-preview.png")

st.header("Triángulo")

st.markdown(""" 

El área de un triángulo es el espacio cerrado en un plano bidimensional por los tres lados de cualquier triángulo.

Para todo triángulo, sin importar su tipo, el área se puede hallar de diferentes maneras, esto dependerá de los datos o información que se conozca del triángulo.

""")
with st.container(border=True):
 c1,c2 =st.columns(2)

 with c1:
  with st.container(border=True):
    st.markdown('formula del área de un triángulo')
    st.latex('A= (b*h)/2)')
    st.markdown('donde **b** es la medida de la base y **h** es la altura del triángulo ')
 with c2:
    st.image("imagenes/triangulo-removebg-preview.png")

st.header("Círculo")

st.markdown(""" 

El área de un círculo es igual al producto de Pi (π) por la medida del radio de la circunferencia elevado al cuadrado.

""")
with st.container(border=True):
 c1,c2 =st.columns(2)

 with c1:
  with st.container(border=True):
    st.markdown('formula del área de un círculo')
    st.latex('A= π*r²')
    st.markdown('donde **r** es la medida del radio del circulo  ')
 with c2:
    st.image("imagenes/area-circulo-removebg-preview.png")

st.header("Trapecio")

st.markdown(""" 

Para hallar su área, se puede se puede considerar el trapecio ABCD de la representación gráfica. Donde el lado **AD** corresponde a la base menor (b) y el lado del trapecio **BC** es la base mayor (B) y la altura h es la longitud del segmento entre **AD** y **BC**, entonces el área se expresa como:

""")
with st.container(border=True):
 c1,c2 =st.columns(2)

 with c1:
  with st.container(border=True):
    st.markdown('formula del área de un trapecio')
    st.latex('A=((b+B)/2)h')
    st.markdown('donde **b** es la medida de la base menor del trapecio, **B** es la base mayor y  **h** es la altura del trapecio ')
 with c2:
    st.image("imagenes/trapecio-removebg-preview.png")

st.header("Rombo")

st.markdown(""" 

Existen varias maneras o fórmulas para calcular el area de un rombo, sin embargo, la mas utilizada es el área es la mitad del producto de las diagonales (d y D). 

""")
with st.container(border=True):
 c1,c2 =st.columns(2)

 with c1:
  with st.container(border=True):
    st.markdown('formula del área de un rombo')
    st.latex('A=(D*d)/2')
    st.markdown('donde **d** y **D** son las diagonales del rombo ')
 with c2:
    st.image("imagenes/rombo-removebg-preview.png")




st.markdown("**Fuentes**")

st.markdown("""

https://www.neurochispas.com/wiki/area-de-un-trapecio/
https://www.universoformulas.com/matematicas/geometria/area-rombo/
https://enciclopediaiberoamericana.com/area/
https://enciclopediaiberoamericana.com/rectangulo/
https://enciclopediaiberoamericana.com/area-de-un-triangulo/
https://economipedia.com/definiciones/area.html

""")