#from functions import read_file,write_file,append_file
import functions as f

while True:
    
    user_prompt = "Enter a todo :"
    todos=[]
    user_opt = input("Enter (add [todo], show , edit [todo no],complete [todo no] or exit):")
    user_opt=user_opt.strip()

    if(user_opt.startswith('add')):

        user_text = user_opt[4:]+"\n"
        f.append_file(user_text)

    elif(user_opt.startswith('show')):
            
        todos=f.read_file()
        
        for i,item in enumerate(todos,start=1):
            print(f"{i}-{item.strip('\n')}")

    elif(user_opt.startswith('edit')):

        try:
            todos=f.read_file()
            
            number = int(user_opt[5:])
            todos[number-1]=input("Enter the new todo:")+"\n"

            f.write_file(todos)

            print(f"Todo is successfully edited!!!\n")
        except ValueError:
            print("Edit command should be followed by the number of todo!!")
            continue

    elif(user_opt.startswith('complete')):

        try:
            number = int(user_opt[9:])
            todos=f.read_file()

            rmv_msg=todos.pop(number-1)
            rmv_msg=rmv_msg.strip('\n')

            f.write_file(todos)

            msg = f"Todo - '{rmv_msg}' is successfully removed!!!\n"
            print(msg)

        except ValueError:
            print("Complete command should be followed by the number of todo!!")
            continue
        except IndexError:
            print("Complete command exceeds the total number of todo!!")
            continue

    elif('exit' in user_opt):
        break

    else:
        print("Command is invalid!!")

