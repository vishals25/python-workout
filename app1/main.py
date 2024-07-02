user_prompt = "Enter a todo :"
todos=[]
while True:

    user_opt = input("Enter (add , see , edit or exit):")
    user_opt=user_opt.strip()

    if(user_opt =='add'):
        user_text = input(user_prompt)
        todos.append(user_text)

    elif(user_opt == 'see'):

        for i in todos:
            print(i.title())

    elif(user_opt == 'edit'):
        number = int(input("number of todo item:"))
        todos[number-1]=input("enter new todo:")

    elif(user_opt == 'exit'):
        break

print("bye!")