num1 = 42 #variable declaration...integer
num2 = 2.3 #variable declaration...float
boolean = True #variable declaration
string = 'Hello World' #variable declaration...string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration....list initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration...dictionary initialize
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration...Tuples
print(type(fruit)) #log the datatype of fruit...which is a tuple
print(pizza_toppings[1]) #log index 1 of pizza toppings which is sausage
pizza_toppings.append('Mushrooms') #add mushrooms to pizza lilt
print(person['name']) #log name from person dictionary
person['name'] = 'George' # change person name from john to george
person['eye_color'] = 'blue' #add eye color to person dictionary
print(fruit[2]) #log index 2 of fruit tuple

if num1 > 45: #if conditional
    print("It's greater") #if conditional is met print this
else:
    print("It's lower") #if it is not met print this instead

if len(string) < 5: #if conditional...length of string variable is less than 5
    print("It's a short word!")#print this
elif len(string) > 15: #else if it is greater than 15 print this instead
    print("It's a long word!")
else: #final part of the conditional
    print("Just right!") #if it does not meet the if or elif print this

for x in range(5): #variable declaration...returns a range of numbers from 0-4
    print(x) #prints those numbers
for x in range(2,5): #variable declaration...returns range of numbers from 2-4
    print(x) #prints those numbers
for x in range(2,10,3): #variable declaration...returns a range of number from 2-9 incremented by 3
    print(x) #prints those numbers
x = 0 #variable declaration
while(x < 5): #while loop...start at x, and as long as it is lower than 5 continue the loop
    print(x) #print x at each iteration of the loop
    x += 1 #increment x by +1 each iteration of the loop

pizza_toppings.pop() #remove last index of the list
pizza_toppings.pop(1) #remove index 1 of the pizza list

print(person) #print person dictionary
person.pop('eye_color') #remove eye color from person dictionary
print(person) #print person dictionary again

for topping in pizza_toppings: #for loop including pizza topping in pizza list
    if topping == 'Pepperoni': # if the topping is pizza continue in the loop
        continue #stop the current iteration of the loop, and continue with the next 
    print('After 1st if statement') #print this
    if topping == 'Olives': #conditional statement
        break #stop the loop

def print_hello_ten_times(): #defines that this is a function w/ no parameters
    for num in range(10): #for loop for numbers ranging from 0 to 9
        print('Hello') #for each number in the range print hello

# print_hello_ten_times() #invoking the function

def print_hello_x_times(x): #defines that this is a function with a parameter of x being accepted
    for num in range(x): #for loop for numbers in range of 0 to x
        print('Hello') #print hello at each iteration of the loop

# print_hello_x_times(4) #invoking the function with the argument of 4 for x

def print_hello_x_or_ten_times(x = 10): #defineds that this is a function of a parameter of x = 10
    for num in range(x): #for loop for numbers ranging from 0 to x
        print('Hello')#print hello at each iteration

print_hello_x_or_ten_times() #invoking function will print hello 10 times
print_hello_x_or_ten_times(4)#invoking function with argument of 4, will print hello 4 times


"""
Bonus section
"""

print(num3) #wont print as python is read top to bottom and variable hasn't been declared yet
num3 = 72
fruit[0] = 'cranberry'
print(person['favorite_team']) #can't alter a tuple
print(pizza_toppings[7]) #index does not exist
print(boolean) #initial indent error
fruit.append('raspberry') #cant alter a tuple
fruit.pop(1)#cant alter a tuple