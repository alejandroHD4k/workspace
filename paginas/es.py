import streamlit as st


    
rta1 = st.selectbox("**1.**¿Qué sucede con el área de un rectángulo si duplicamos tanto su ancho como su altura?", ["", "El área se multiplica por 2", "El área se multiplica por 3", "El área se cuadruplica", " El área no cambia"]) 
c1 = st.empty()

rta2 = st.selectbox("**2.** Si un triángulo tiene una base de 8 metros y una altura de 5 metros, ¿cuál es su área?", ["", "40 metros cuadrados", "30 metros cuadrados", "20 metros cuadrados", "18 metros cuadrados"])
c2 = st.empty()

rta3 = st.selectbox("**3.**¿Cuál es la fórmula para calcular el área de un círculo?", ["", "A= π*r²", "A=2πr", "A= π*r³", "A= ((b+B)/2)h"])
c3 = st.empty()

rta4 = st.selectbox("**4.**¿Qué sucede con el área de un trapecio si duplicamos la altura pero mantenemos las bases iguales?", ["", "El área se multiplica por 2", "El área se cuadruplica", "El área no cambia", "El área se reduce a la mitad"] )
c4= st.empty()

rta5 = st.selectbox("**5.**¿Cuál es el área de un triángulo con base de 12 metros y altura de 7 metros?", ["", "42 metros cuadrados", "84 metros cuadrados", "36 metros cuadrados", "48 metros cuadrados"] )
c5= st.empty()

rta6 = st.selectbox("**6.**¿Cuál es la fórmula general para calcular el volumen de un prisma?", ["", "V= 1/4(15+7√5)a³", "1/3 √2a³", "V= Ab * h", "V= a³ "])
c6 = st.empty()

rta7 = st.selectbox("**7.** Si un cubo tiene una arista de longitud 5 cm, ¿cuál es su volumen?", ["", "25 cm³", "75 cm³", "125 cm³", "150 cm³"])
c7 = st.empty()

rta8 = st.selectbox("**8.** Un cilindro tiene un radio de 3 cm y una altura de 10 cm. ¿Cuál es su volumen?(Usa 𝜋=3.1416)", ["","282.6 cm³", " 314 cm³", "188.4 cm³", "94.2 cm³" ])
c8 = st.empty()

rta9 = st.selectbox("**9.** El volumen de una pirámide se obtiene multiplicando el área de la base por la altura y dividiendo por:", ["", "3", "4", "6", "2"] )
c9= st.empty()

rta10 = st.selectbox("**10.**¿Qué información necesitas conocer para calcular el volumen de un tetraedro regular?", ["", "La longitud de sus aristas", " El área de su base y la altura", "El radio de su base", "El perímetro de la base"] )
c10= st.empty()


ptos = 0

if st.button("Verificar"):

  if rta1 == "El área se cuadruplica":
      c1.info("¡excelente!")
      ptos += 0.5
  else:
        c1.error("Incorrecto")
    
  if rta2 == "20 metros cuadrados":
        c2.info("¡excelente!")
        ptos += 0.5
  else:
        c2.error("Incorrecto")
    
  if rta3 == "A= π*r²":
        c3.info("¡excelente!")
        ptos += 0.5
  else:
        c3.error("Incorrecto")

  if rta4 == "El área se multiplica por 2":
        c4.info("¡excelente!")
        ptos += 0.5
  else:
        c4.error("Incorrecto")

  if rta5 == "42 metros cuadrados":
        c5.info("¡excelente!")
        ptos += 0.5
  else:
     c5.error("Incorrecto")

  if rta6 == "V= Ab * h":
        c6.info("¡excelente!")
        ptos += 0.5
  else:
        c6.error("Incorrecto")
    
  if rta7 == "125 cm³":
        c7.info("¡excelente!")
        ptos += 0.5
  else:
        c7.error("Incorrecto")
    
  if rta8 == "282.6 cm³":
        c8.info("¡exccelente!")
        ptos += 0.5
  else:
        c8.error("Incorrecto")

  if rta9 == "3":
        c9.info("¡excelente!")
        ptos += 0.5
  else:
        c9.error("Incorrecto")

  if rta10 == "La longitud de sus aristas":
        c10.info("¡excelente!")
        ptos += 0.5
  else:
        c10.error("Incorrecto")

st.markdown(f"Tu calificacion es: {ptos}")