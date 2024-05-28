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

# Função para enviar uma mensagem
def send_message(sender, recipient, message):
    with open(f"{sender}_messages.txt", "a") as file:
        file.write(f"{recipient}:{message}\n")

# Função para obter mensagens recebidas por um usuário
def get_messages(username):
    messages = []
    try:
        with open(f"{username}_messages.txt", "r") as file:
            for line in file:
                recipient, message = line.strip().split(":")
                messages.append((recipient, message))
    except FileNotFoundError:
        pass
    return messages

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
            st.session_state.username = username
            st.success("Login bem-sucedido!")
        else:
            st.error("Usuário ou senha incorretos")

# Componentes para envio e recebimento de mensagens
if st.session_state.get("logged_in", False):
    st.subheader("Conversa")
    
    # Lista de usuários registrados
    registered_users = [line.strip().split(",")[0] for line in open("users.txt", "r")]
    recipient = st.selectbox("Enviar mensagem para:", registered_users)
    
    message = st.text_input("Mensagem")
    if st.button("Enviar"):
        send_message(st.session_state.username, recipient, message)
        st.success(f"Mensagem enviada para {recipient}")
    
    st.subheader("Mensagens Recebidas")
    messages = get_messages(st.session_state.username)
    for sender, message in messages:
        st.write(f"{sender}: {message}")
