import streamlit as st

st.title("Áreas y Volumenes")
st.caption("teoria e historia de areas y volumenes ")


st.header("Áreas") 

st.markdown("""

como vimos anteriormente las areas en geometría sonla medida de un espacio delimitado por un contorno al qie se le denomina perímetro.

Muchas veces se usa de manera indistinta las palabras **superficie** y **área**, ya que para muchos es como si fueran lo mismo. Y aunque están relacionadas, hay una diferencia sutil entre ellas.

La superficie se refiere al espacio en sí, como por ejemplo el que abarca un campo o una casa. Por otro lado, el área es la medida de cuánto espacio ocupa esa superficie. Por ejemplo, podríamos medir el área del campo en hectáreas.

La medida del **área** de la figura, se expresa en unidades cuadradas, por ejemplo, metros cuadrados (mts2), centímetros cuadrados (cm2), pulgadas cuadradas (in2), entre otras medidas de longitud, pero siempre expresadas al cuadrado, ya que esta se mide en un espacio de solo dos dimenciones, osea, un plano.

Conocer el área de una figura geométrica, es importante en la aplicación de las matemáticas, como álgebra, trigonometría. Permitiendo calcular el espacio que ocupa cualquier superficie para su empleo en la arquitectura, diseño gráfico, ingeniería, entre otras.

En geometría, conocer el área es muy útil, ya que nos ayuda a entender cuánto espacio tenemos disponible. Por ejemplo, si sabemos el área de un terreno agrícola, podemos calcular cuánto podemos plantar, así como la cantidad de agua y fertilizante que necesitaremos.

""")

c1,c2 =st.columns(2)

with c1:
    st.video('https://youtu.be/jhY_5JzZyU4')


with c2:
    st.image('imagenes/area-removebg-preview.png')



st.subheader("Historia de las áreas")

st.markdown("""
La idea de que el área es la medida que proporciona el tamaño de la región encerrada en una figura geométrica proviene de la antigüedad. En el antiguo Egipto, tras la crecida anual de río Nilo inundando los campos, surge la necesidad de calcular el área de cada parcela agrícola para restablecer sus límites; para solventar eso, los egipcios inventaron la geometría, según Heródoto.

El modo de calcular el área de un polígono como la suma de las áreas de los triángulos, es un método que fue propuesto por primera vez por el sabio griego Antifón hacia el año 430 a. C. Hallar el área de una figura curva genera más dificultad. El método exhaustivo consiste en inscribir y circunscribir polígonos en la figura geométrica, aumentar el número de lados de dichos polígonos y hallar el área buscada. Con el sistema que se conoce como método exhaustivo de Eudoxo, consiguió obtener una aproximación para calcular el área de un círculo. Dicho sistema fue empleado tiempo después por Arquímedes para resolver otros problemas similares, así como el cálculo aproximado del número π.
""")




st.header("Volumenes") 

st.markdown("""
Se entiende por volumen a una magnitud métrica, euclideana y de tipo escalar, que se puede definir como la extensión de un objeto en sus tres dimensiones, es decir, tomando en cuenta su longitud, ancho y altura. Todos los cuerpos físicos ocupan un espacio que varía según sus proporciones, y la medida de dicho espacio es el volumen.

Para calcular el volumen de un objeto bastará con multiplicar su longitud por su ancho y por su altura, o en el caso de sólidos geométricos, aplicar determinadas fórmulas a partir del área y la altura u otras variables parecidas.


""")



c1,c2 =st.columns(2)

with c1:
    st.video('https://youtu.be/1IO8oZkrkXI')


with c2:
    st.image('imagenes/volumenes-removebg-preview.png')


st.subheader("Historia de los volumenes")

st.markdown("""
 Las primeras evidencias de cálculo de volumen proceden del antiguo Egipto y Mesopotamia como problemas matemáticos, aproximando el volumen de formas simples como cuboides, cilindros, frustum y conos. Estos problemas matemáticos han sido escritos en el Papiro Matemático de Moscú (c. 1820 a. C.).En el Papiro Reisner, los antiguos egipcios han escrito unidades concretas de volumen para granos y líquidos, así como una tabla de longitud, anchura, profundidad y volumen para bloques de material.

""")

st.markdown("**Fuentes**")

st.markdown('https://economipedia.com/definiciones/area.html')
