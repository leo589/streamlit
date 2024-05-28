import streamlit as st

# Título da página
st.title("Streamlit YouTube Video Player")

# Entrada de texto para o link do YouTube
youtube_url = st.text_input("Insira o link do YouTube")

# Verifica se o URL foi inserido
if youtube_url:
    # Exibe o vídeo
    st.video(youtube_url)
else:
    st.write("Por favor, insira um link válido do YouTube.")

# Para rodar essa aplicação, salve este código em um arquivo app.py
# e execute o comando 'streamlit run app.py' no terminal.
