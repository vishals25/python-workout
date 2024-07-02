user_prompt = "Enter a todo :"
todos=[]
while True:

    user_opt = input("Enter (add , show , edit ,complete or exit):")
    user_opt=user_opt.strip()

    if(user_opt =='add'):
        user_text = input(user_prompt)
        todos.append(user_text)

    elif(user_opt == 'show'):

        for i,item in enumerate(todos,start=1):
            print(f"{i}-{item}")

    elif(user_opt == 'edit'):
        number = int(input("Number of todo item to edit:"))
        todos[number-1]=input("Enter the new todo:")
    
    elif(user_opt == 'complete'):
        number = int(input("Number of todo item to complete:"))
        todos.pop(number-1)

    elif(user_opt == 'exit'):
        break
