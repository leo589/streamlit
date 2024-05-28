import streamlit as st
import socketio
import eventlet
from threading import Thread

# Inicializa o servidor Socket.IO
sio = socketio.Server()
app = socketio.WSGIApp(sio)

# Dicionário para armazenar os usuários registrados
registered_users = {}

# Função para processar a conexão de um novo cliente
@sio.on('connect')
def connect(sid, environ):
    print('Client connected:', sid)

# Função para processar a desconexão de um cliente
@sio.on('disconnect')
def disconnect(sid):
    print('Client disconnected:', sid)

# Função para lidar com a autenticação do usuário
@sio.on('login')
def login(sid, data):
    username = data['username']
    password = data['password']
    if username in registered_users and registered_users[username] == password:
        sio.emit('login_response', {'success': True}, room=sid)
    else:
        sio.emit('login_response', {'success': False, 'message': 'Usuário ou senha incorretos'}, room=sid)

# Função para lidar com o registro de novos usuários
@sio.on('register')
def register(sid, data):
    username = data['username']
    password = data['password']
    if username not in registered_users:
        registered_users[username] = password
        sio.emit('register_response', {'success': True}, room=sid)
    else:
        sio.emit('register_response', {'success': False, 'message': 'Nome de usuário já registrado'}, room=sid)

# Função para enviar mensagens entre os usuários
@sio.on('send_message')
def send_message(sid, data):
    recipient = data['recipient']
    message = data['message']
    sio.emit('receive_message', {'sender': sid, 'message': message}, room=recipient)

# Função para executar o servidor Socket.IO
def run_server():
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)

# Inicia o servidor em uma thread separada
server_thread = Thread(target=run_server)
server_thread.start()

# Interface Streamlit
st.title("Chat em Tempo Real")

# Componentes para login/registro de usuário
option = st.sidebar.radio("Escolha uma opção:", ("Login", "Registro"))
username = st.text_input("Nome de Usuário")
password = st.text_input("Senha", type="password")
if option == "Login":
    if st.button("Entrar"):
        sio.emit('login', {'username': username, 'password': password})
        response = sio.get_sid_namespace().wait_for_callbacks(timeout=5)
        if response and response[0]['name'] == 'login_response' and response[0]['args'][0]['success']:
            st.success("Login bem-sucedido!")
        else:
            st.error("Usuário ou senha incorretos")
elif option == "Registro":
    if st.button("Registrar"):
        sio.emit('register', {'username': username, 'password': password})
        response = sio.get_sid_namespace().wait_for_callbacks(timeout=5)
        if response and response[0]['name'] == 'register_response' and response[0]['args'][0]['success']:
            st.success("Registro bem-sucedido!")
        else:
            st.error("Nome de usuário já registrado")

# Componentes para envio e recebimento de mensagens
if st.session_state.logged_in:
    st.subheader("Conversa")
    recipient = st.selectbox("Enviar mensagem para:", list(registered_users.keys()))
    message = st.text_input("Mensagem")
    if st.button("Enviar"):
        sio.emit('send_message', {'recipient': recipient, 'message': message})

# Lógica para mudar para uma conversa diferente
change_conversation = st.button("Mudar de Conversa")
if change_conversation:
    st.session_state.logged_in = not st.session_state.logged_in
