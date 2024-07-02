user_prompt = "Enter a todo :"
todos=[]
while True:

    user_opt = input("Enter (add , show , edit ,complete or exit):")
    user_opt=user_opt.strip()

    if(user_opt.startswith('add')):

        user_text = user_opt[4:]+"\n"

        with open('todo.txt','a+') as file:
            file.writelines(user_text)

    elif('show' in user_opt):

        with open('todo.txt','r') as file:
            todos=file.readlines()
        
        for i,item in enumerate(todos,start=1):
            print(f"{i}-{item.strip('\n')}")

    elif('edit' in user_opt):

        with open('todo.txt','r') as file:
            todos=file.readlines()
        
        number = int(input("Number of todo item to edit:"))
        todos[number-1]=input("Enter the new todo:")+"\n"

        with open('todo.txt','w') as file:
            file.writelines(todos)

        print(f"Todo is successfully edited!!!\n")

    elif('complete' in user_opt):

        number = int(input("Number of todo item to complete:"))

        with open('todo.txt','r') as file:
            todos=file.readlines()

        rmv_msg=todos.pop(number-1)
        rmv_msg=rmv_msg.strip('\n')

        with open('todo.txt','w') as file:
            file.writelines(todos)

        msg = f"Todo - '{rmv_msg}' is successfully removed!!!\n"
        print(msg)

    elif('exit' in user_opt):
        break
