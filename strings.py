# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


# String Formatting


name = "Michelle"
age = 22

# concatenate 
print('Hello my name is ' + name + " I am " + str(age) + " years." )


# string formatting

#1. Arguments by postion 
print("My name is {name}; I am {age}" .format(name = name, age = age))

# 2. Using f strings 
print(f'Hello, my name is {name} and I am {age }')


# String Methods
