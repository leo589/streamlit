import streamlit as st

# Função para carregar dados de um arquivo .txt
def load_data(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.readlines()
        return [line.strip().split(",") for line in data]
    except FileNotFoundError:
        return []

# Função para salvar dados em um arquivo .txt
def save_data(file_name, data):
    with open(file_name, "w") as file:
        for entry in data:
            file.write(",".join(entry) + "\n")

# Função para adicionar um aluno
def add_student(name, age, grade, file_name="students.txt"):
    students = load_data(file_name)
    students.append([name, str(age), grade])
    save_data(file_name, students)

# Função para listar alunos
def list_students(file_name="students.txt"):
    return load_data(file_name)

# Interface Streamlit
st.title("Gerenciamento Escolar")

menu = st.sidebar.selectbox("Menu", ["Adicionar Aluno", "Listar Alunos"])

if menu == "Adicionar Aluno":
    st.header("Adicionar Aluno")
    name = st.text_input("Nome")
    age = st.number_input("Idade", min_value=1, max_value=100, step=1)
    grade = st.selectbox("Série", ["1ª Série", "2ª Série", "3ª Série"])
    if st.button("Adicionar"):
        add_student(name, age, grade)
        st.success("Aluno adicionado com sucesso!")

elif menu == "Listar Alunos":
    st.header("Lista de Alunos")
    students = list_students()
    if students:
        df = pd.DataFrame(students, columns=["Nome", "Idade", "Série"])
        st.dataframe(df)
    else:
        st.write("Nenhum aluno cadastrado.")
