import streamlit as st
import functions as f

def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    f.append_file(todo)
    st.session_state["new_todo"] = ''

todos=f.read_file()

st.title("My To-Do App")

st.text_input(label="Enter A Todo:",placeholder='example:buy a car',on_change=add_todo,key='new_todo')

for item,todo in enumerate(todos):
    check=st.checkbox(todo,key=item)
    if(check):
        todos.pop(item)
        f.write_file(todos)
        del(st.session_state[item])
        st.rerun()
