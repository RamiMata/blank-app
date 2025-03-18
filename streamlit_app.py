import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener API Key desde el archivo .env
openai.api_key = os.getenv("OPENAI_API_KEY")

# Título de la aplicación
st.title("PostGenius - Generador de Ideas para Redes Sociales")
st.write("Bienvenido a PostGenius, la herramienta que utiliza inteligencia artificial para ayudarte a generar ideas de contenido para tus redes sociales.")

# Sección "Cómo funciona"
st.header("Cómo funciona")
st.write("""
1. Ingresa tu nicho de contenido (ejemplo: fitness, tecnología, moda).
2. Selecciona la plataforma para la cual deseas generar ideas (Instagram, TikTok, Twitter, YouTube, LinkedIn).
3. Elige el objetivo de la publicación (engagement, atraer seguidores, generar ventas, educar a la audiencia).
4. Selecciona el formato de contenido (imagen, carrusel, video, historia, encuesta, reel).
5. Presiona el botón para generar ideas y obtendrás cinco sugerencias para tus publicaciones.
""")

# Inputs del usuario
nicho = st.text_input("Nicho de contenido")
plataforma = st.selectbox("Selecciona la plataforma", ["Instagram", "TikTok", "Twitter", "YouTube", "LinkedIn"])
objetivo = st.selectbox("Elige el objetivo de la publicación", ["Engagement", "Atraer seguidores", "Generar ventas", "Educar a la audiencia"])
formato = st.selectbox("Selecciona el formato de contenido", ["Imagen", "Carrusel", "Video", "Historia", "Encuesta", "Reel"])

# Función para generar ideas
def generar_ideas(nicho, plataforma, objetivo, formato):
    prompt = f"Genera cinco ideas de publicaciones para una cuenta de {plataforma} sobre {nicho} cuyo objetivo es {objetivo}. Formato: {formato}."
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            n=1,
            stop=None,
            temperature=0.7
        )
        ideas = response.choices[0].text.strip().split('\n')
        return ideas
    except Exception as e:
        st.error("Error al generar ideas. Por favor, intenta nuevamente.")
        return []

# Botón para generar ideas
if st.button("Generar Ideas"):
    if not nicho or not plataforma or not objetivo or not formato:
        st.error("Por favor, completa todos los campos.")
    else:
        ideas = generar_ideas(nicho, plataforma, objetivo, formato)
        if ideas:
            st.header("Ideas Generadas")
            for i, idea in enumerate(ideas, start=1):
                st.subheader(f"Idea {i}")
                st.write(idea)

st.write("© 2025 PostGenius. Todos los derechos reservados.")
