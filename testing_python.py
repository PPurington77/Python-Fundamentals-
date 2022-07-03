# import random 
# print('Welcome to Python!')

# print('This is a loop printing 5 times')
# for x in range(1, 6):
#     print(f'x is: {x}')

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# day = random.choice(weekdays)
# print(f'Today is: {day}')

# if day == 'Monday':
#     print('It will be a long week!')
# elif(day == 'Friday'):
#     print('Woohoo, time for the weekend!')
# else:
#     print('Not quite there yet.')

# print(type(24))
# print(type(3.9))
# print(type(3j))

# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

# import random 
# print(random.randint(2,5))

# print("this is a simple string")

# name = "Patrick"
# print("My name is", name)
# print("My name is " + name)

# num = 10
# print("the number is", num)
# print("the number is " + num)

# print("hello" + 42) ///cant combine strings and integers
# print("hello " + str(42)) integer is converted into a string with str 

# total = 35
# user_val = "26"
# total = total + user_val //cant combine numbers with strings
# total = total + int(user_val) //converts the string into an integer 
# print(total)

#string interpolation/// below is F-Strings. to create f string place f before opening "" the within the string place variables within curly braces

# first_name = "Patrick"
# last_name = "Purington" 
# age = 30
# print(f"my name is {first_name} {last_name} and I am {age} years old")

#string.format() is the old way of doing it before f strings were a thing to use follow below
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))

# %formatting..even older than string.format % is used instead of {}, a %s for a string, and %d for a number, after the string a % is entered to seperate the the string from the values to be inserted
# hw = "Hello %s" % "world"
# py = "I love python %d" % 3
# print(hw, py)

# name = "Patrick"
# age = 30
# print("My name is %s and I'm %d" % (name, age))


# Built in string methods
# x = "hello world"
# print(x)
# print(x.title()) makes first letter capitalized