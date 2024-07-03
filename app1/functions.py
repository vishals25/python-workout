filepath="todo.txt"
def read_file():
    with open(filepath,'r') as file_loc:
        todos_local=file_loc.readlines()
    return todos_local


def write_file(user_text):
    with open(filepath,'w') as file_loc:
        file_loc.writelines(user_text)

def append_file(user_text):
    with open(filepath,'a+') as file_loc:
        file_loc.writelines(user_text)
