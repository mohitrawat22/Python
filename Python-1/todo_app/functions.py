def getTodos(filepath='E:/Projects/Python/Python-1/todo_app/todos.txt'):
    with open(filepath, 'r') as file:
            todos = file.readlines()
    return todos

def writeTodos(todos, filepath='E:/Projects/Python/Python-1/todo_app/todos.txt'):
    with open(filepath, 'w') as file:
            file.writelines(todos)