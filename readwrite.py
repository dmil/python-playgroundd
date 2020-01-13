# 1. reads name.txt into a variable my_name

with open('name.txt') as f:
    my_name = f.read()

introduction = "Hello, my name is " + my_name


# 2. writes a new file named hello.txt with the contents 
# Hello, my name is <my_name>.

with open('hello.txt', 'w') as f:
    f.write(introduction)
    f.write('\n')


# by: Dhrumil And Sultan