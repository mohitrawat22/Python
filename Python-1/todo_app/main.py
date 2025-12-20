# user input
# print("Enter a todo: ")
# user_input = input()
# print(user_input)

# user_input = input("Enter a todo: ")
# print(user_input)

# multiple user input
# user_prompt = "Enter a todo: "
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)

# todos = [todo1, todo2, todo3]
# print(todos)
# print(type(todos))

# # multiple user input in a loop
# user_prompt = "Enter a todo: "
# while True:
#     todo = input(user_prompt)
#     print(todo)
#     print("Next ...")

# multiple user input in a list
# user_prompt = "Enter a todo: "
# todos = []
# while True:
#     todo = input(user_prompt)
#     todos.append(todo)
#     print(todos)
#     print("Next ...")

# user input conditions
# user_prompt = "Enter a todo: "
# todos = []
# while True:
#     user_action = input("Type add, show or exit: ")
#     user_action = user_action.strip()
#     match user_action:
#         case 'add':
#             todo = input(user_prompt)
#             todos.append(todo)
#         case 'show' | 'display':
#             print(todos)
#         case 'edit':
#             index = int(input("Enter the index of todo to edit: "))
#             todos[index-1] = input("Enter new todo: ")
#         case 'exit':
#             break
#         case _:
#             print('Please enter correct option ... ')

# tuples
# words = ('a', 'b', 'c', 'd')
# print(words[2])
# below will cause exception because tuples cannot be modified
# words[2] = 'm'

# print index and item using enumerate
# for index, item in enumerate(list1):
#     print(index, item)
# user_prompt = "Enter a todo: "
# todos = []
# while True:
#     user_action = input("Type add, show , edit, complete or exit: ")
#     user_action = user_action.strip()
#     match user_action:
#         case 'add':
#             todo = input(user_prompt)
#             todos.append(todo)
#         case 'show' | 'display':
#             for index, item in enumerate(todos):
#                 # print(index, '-', item)
#                 # f-string
#                 row = f"{index+1}-{item}"
#                 print(row)
#         case 'edit':
#             index = int(input("Enter the index of todo to edit: "))
#             todos[index-1] = input("Enter new todo: ")
#         case 'complete':
#             todo_num = int(input('Number of todo to complete: '))
#             todos.pop(todo_num-1)
#         case 'exit':
#             break
#         case _:
#             print('Please enter correct option ... ')

# read/write todo list in a file
# user_prompt = "Enter a todo: "
# while True:
#     user_action = input("Type add, show , edit, complete or exit: ")
#     user_action = user_action.strip()
#     match user_action:
#         case 'add':
#             todo = input(user_prompt) + "\n"

#             file = open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'r')
#             todos = file.readlines()
#             file.close()
            
#             todos.append(todo)

#             file = open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'w')
#             file.writelines(todos)
#             file.close()
#         case 'show' | 'display':
#             file = open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'r')
#             todos = file.readlines()
#             file.close()
#             # new_todos = [item.strip() for item in todos]
#             # for index, item in enumerate(new_todos):
#             #     row = f"{index+1}-{item}"
#             #     print(row)
#             for index, item in enumerate(todos):
#                 item = item.strip()
#                 row = f"{index+1}-{item}"
#                 print(row)
#         case 'edit':
#             index = int(input("Enter the index of todo to edit: "))
#             todos[index-1] = input("Enter new todo: ")
#         case 'complete':
#             todo_num = int(input('Number of todo to complete: '))
#             todos.pop(todo_num-1)
#         case 'exit':
#             break
#         case _:
#             print('Please enter correct option ... ')

# read/write todo list in a file
# usage of "with"
user_prompt = "Enter a todo: "
while True:
    user_action = input("Type add, show , edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':

            todo = input(user_prompt) + "\n"

            with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'r') as file:
                todos = file.readlines()
            
            todos.append(todo)

            with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            
            with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip() for item in todos]
            # for index, item in enumerate(new_todos):
            #     row = f"{index+1}-{item}"
            #     print(row)
            for index, item in enumerate(todos):
                item = item.strip()
                row = f"{index+1}-{item}"
                print(row)
        
        case 'edit':

            index = int(input("Enter the index of todo to edit: "))
            with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'r') as file:
                todos = file.readlines()
            todos[index-1] = input("Enter new todo: ") + "\n"
            with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'w') as file:
                file.writelines(todos)
        
        case 'complete':

            todo_num = int(input('Number of todo to complete: '))
            with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'r') as file:
                todos = file.readlines()
            todo_to_remove = todos[todo_num-1].strip()
            todos.pop(todo_num-1)
            with open('E:/Projects/Python/Python-1/todo_app/todos.txt', 'w') as file:
                file.writelines(todos)
                print(f'Todo {todo_to_remove} was removed from the list.')

        case 'exit':
            break

        case _:
            print('Please enter correct option ... ')
