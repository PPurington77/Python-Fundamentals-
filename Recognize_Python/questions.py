pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
print(pizza_toppings)

pizza_toppings.append('Mushrooms')
print(pizza_toppings)

pizza_toppings.pop() #remove last index of the list
print(pizza_toppings)

pizza_toppings.pop(1)
print(pizza_toppings)


for topping in pizza_toppings: #for loop including pizza topping in pizza list
    if topping == 'Pepperoni': # if the topping is pizza continue in the loop
        continue #stop the current iteration of the loop, and continue with the next 
    print('After 1st if statement') #print this
#     if topping == 'Olives': #conditional statement
#         break #stop the loop
