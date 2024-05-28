import streamlit as st
from bs4 import BeautifulSoup  # Certifique-se de que este import está correto

def main():
    st.title("Conversor de HTML e CSS para Página Streamlit")

    # Área de texto para entrada do HTML
    html_input = st.text_area("Insira o código HTML aqui:", height=300)
    # Área de texto para entrada do CSS
    css_input = st.text_area("Insira o código CSS aqui:", height=100)

    if st.button("Converter e Renderizar"):
        if html_input:
            # Converter HTML para elementos Streamlit
            render_html(html_input, css_input)
        else:
            st.warning("Por favor, insira o código HTML para conversão.")

def render_html(html_code, css_code):
    # Usando BeautifulSoup para processar o HTML
    soup = BeautifulSoup(html_code, 'html.parser')

    # Aplica estilos CSS (embora limitado em Streamlit)
    if css_code:
        st.markdown(f"<style>{css_code}</style>", unsafe_allow_html=True)

    # Renderizar elementos HTML individualmente
    for element in soup.body:
        if element.name == "h1":
            st.header(element.text)
        elif element.name == "h2":
            st.subheader(element.text)
        elif element.name == "p":
            st.write(element.text)
        elif element.name == "img":
            img_src = element.get('src')
            if img_src:
                st.image(img_src)
        elif element.name == "a":
            link_text = element.text
            link_href = element.get('href')
            if link_href:
                st.markdown(f"[{link_text}]({link_href})", unsafe_allow_html=True)
        else:
            st.markdown(str(element), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
