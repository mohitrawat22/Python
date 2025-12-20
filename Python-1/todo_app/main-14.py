from functions import getTodos, writeTodos

# filepath = 'E:/Projects/Python/Python-1/todo_app/todos.txt'
user_prompt = "Enter a todo: "
while True:
    user_action = input("Type add, show , edit, complete or exit: ")
    user_action = user_action.strip()
    if 'add' in user_action:

        todo = user_action[4:]
        todos = getTodos()
        todos.append(todo+"\n")
        writeTodos(todos)

    elif 'show' in user_action:
        
        todos = getTodos()
        for index, item in enumerate(todos):
            item = item.strip()
            row = f"{index+1}-{item}"
            print(row)

    elif 'edit' in user_action:
        try:
            index = int(user_action[5:])
            todos = getTodos()
            todos[index-1] = input("Enter new todo: ") + "\n"
            writeTodos(todos)
        except ValueError:
            print('Enter a valid number')
            continue

    elif 'complete' in user_action:

        todo_num = int(user_action[9:])
        todos = getTodos()
        todo_to_remove = todos[todo_num-1].strip()
        todos.pop(todo_num-1)
        writeTodos(todos)
        print(f'Todo {todo_to_remove} was removed from the list.')

    elif 'exit' in user_action:
        break

    else:
        print('Command is invalid')