import streamlit as st
from Functions import get_todos, write_todos

todos = get_todos()
def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    write_todos(todos)


st.title("My Todo App")
st.subheader('')
st.write('')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st._experimental_rerun()

st.text_input(label="Enter a todo:",
              placeholder="Enter a todo:",
              on_change=add_todo,
              key='new_todo')

