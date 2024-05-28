import streamlit as st

# Função para verificar o login
def login(username, password):
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if username == stored_username and password == stored_password:
                return True
    return False

# Função para a tela de login
def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.success("Login successful!")
            return True
        else:
            st.error("Invalid username or password.")
    return False

# Função para a tela de seleção de filmes
def movie_selection():
    st.title("Movie Selection")
    st.write("Welcome to our movie selection!")

    # Aqui você pode adicionar o código para exibir os filmes disponíveis e permitir que o usuário faça sua seleção.

def main():
    if not login_page():
        return

    movie_selection()

if __name__ == "__main__":
    main()
