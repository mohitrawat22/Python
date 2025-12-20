# usage of if-else, instead of case
user_prompt = "Enter a todo: "
while True:
    user_action = input("Type add, show , edit, complete or exit: ")
    user_action = user_action.strip()
    if 'add' in user_action:

        todo = user_action[4:]

        with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'r') as file:
            todos = file.readlines()
        
        todos.append(todo+"\n")

        with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        
        with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip()
            row = f"{index+1}-{item}"
            print(row)

    elif 'edit' in user_action:

        index = int(user_action[5:])
        with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'r') as file:
            todos = file.readlines()
        todos[index-1] = input("Enter new todo: ") + "\n"
        with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:

        todo_num = int(user_action[9:])
        with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'r') as file:
            todos = file.readlines()
        todo_to_remove = todos[todo_num-1].strip()
        todos.pop(todo_num-1)
        with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'w') as file:
            file.writelines(todos)
            print(f'Todo {todo_to_remove} was removed from the list.')

    elif 'exit' in user_action:
        break

    else:
        print('Command is invalid')