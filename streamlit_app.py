import streamlit as st

# Dicionário para armazenar os usuários registrados
registered_users = {}

# Função para registrar um novo usuário
def register_user(username, password):
    if username not in registered_users:
        registered_users[username] = password
        return True
    else:
        return False

# Função para autenticar um usuário
def authenticate_user(username, password):
    if username in registered_users:
        if registered_users[username] == password:
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
        if register_user(username, password):
            st.success("Registro bem-sucedido!")
        else:
            st.error("Nome de usuário já registrado")
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
    recipient = st.selectbox("Enviar mensagem para:", list(registered_users.keys()))
    message = st.text_input("Mensagem")
    if st.button("Enviar"):
        st.success(f"Mensagem enviada para {recipient}: {message}")

# Lógica para mudar para uma conversa diferente
change_conversation = st.button("Mudar de Conversa")
if change_conversation:
    st.session_state.logged_in = not st.session_state.logged_in
