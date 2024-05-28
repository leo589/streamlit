import streamlit as st

# Função para registrar um novo usuário
def register_user(username, password):
    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")

# Função para autenticar um usuário
def authenticate_user(username, password):
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if stored_username == username and stored_password == password:
                return True
    return False

# Interface Streamlit
st.title("Chat em Tempo Real")

# Componentes para login/registro de usuário
option = st.sidebar.radio("Escolha uma opção:", ("Login", "Registro"))
username = st.text_input("Nome de Usuário")
password = st.text_input("Senha", type="password")
if option == "Registro":
    if st.button("Registrar"):
        register_user(username, password)
        st.success("Registro bem-sucedido!")
elif option == "Login":
    if st.button("Entrar"):
        if authenticate_user(username, password):
            st.session_state.logged_in = True
            st.success("Login bem-sucedido!")
        else:
            st.error("Usuário ou senha incorretos")

# Componentes para envio e recebimento de mensagens
if st.session_state.get("logged_in", False):
    st.subheader("Conversa")
    recipient = st.selectbox("Enviar mensagem para:", ["Usuário1", "Usuário2", "Usuário3"])
    message = st.text_input("Mensagem")
    if st.button("Enviar"):
        st.success(f"Mensagem enviada para {recipient}: {message}")

# Lógica para mudar para uma conversa diferente
change_conversation = st.button("Mudar de Conversa")
if change_conversation:
    st.session_state.logged_in = not st.session_state.logged_in
