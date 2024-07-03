import functions as f
import time
import FreeSimpleGUI as g

g.theme("DarkPurple4")

clock=g.Text('',key='clock')
label=g.Text(text='Enter a New Todo : ')

input_box=g.InputText(tooltip="Enter Todo",key='todo',size=[47,1])

add_button=g.Button(button_text="add",border_width=0,size=[6,1])

list_box=g.Listbox(values=f.read_file(),key='exist_todo',enable_events=True,size=[45,10])

edit_button=g.Button(button_text="edit",border_width=0,size=[6,1])

complete_button=g.Button(button_text="complete",border_width=0,size=[12,1])

exit_button=g.Button(button_text="exit",border_width=0,size=[6,1])


window=g.Window(title="My To-Do App",
                layout=[[clock],
                        [label],
                        [input_box,add_button],
                        [list_box,edit_button,complete_button],
                        [exit_button]],
                        font=('Helvetica',13))

while True:
    event, values = window.read(timeout=200) # type: ignore

    if (event == g.WIN_CLOSED):

        break

    window['clock'].update(value=time.strftime("%b %d, %Y : %H-%M-%S")) # type: ignore

    if (event == "add"):

        add_todo=values['todo']+"\n"
        f.append_file(add_todo)

        add_todo=f.read_file()
        window['exist_todo'].update(values=add_todo) # type: ignore

    elif (event == "edit") :

        try:    
            edit_todo = values["exist_todo"][0]
            new_todo = values['todo']+'\n'

            add_todo=f.read_file()
            index=add_todo.index(edit_todo)
            add_todo[index]=new_todo

            f.write_file(add_todo)

            window['exist_todo'].update(values=add_todo) # type: ignore

        except IndexError:
            g.popup("Please select a todo to edit!!",font=('Helvetica',13))

    elif (event =="exist_todo"):

        window["todo"].update(value=values["exist_todo"][0]) # type: ignore

    elif (event == "complete") :

        try:
            edit_todo = values["exist_todo"][0]

            complete_todo = f.read_file()
            index=complete_todo.index(edit_todo)

            complete_todo.pop(index)
            f.write_file(complete_todo)

            window['exist_todo'].update(values=complete_todo) # type: ignore

            window['todo'].update(value='') # type: ignore

        except IndexError:
            g.popup("Please select a todo to complete!!",font=('Helvetica',13))


    elif (event == "exit") :

        break

        
window.close()