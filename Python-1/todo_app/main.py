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
words = ('a', 'b', 'c', 'd')
print(words[2])
# below will cause exception because tuples cannot be modified
# words[2] = 'm'
