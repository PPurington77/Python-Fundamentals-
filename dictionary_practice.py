# 1. Update values in dictionaries and list
# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]

# #1. change the value 10 in x to 15

# x[1][0] = 15
# # print(x)

# #2. Change the last name of the first student from jordan to bryant
# students[0]['last_name'] = 'Bryant'
# # print(students)

# #3. in the sports directory change messi to andres
# sports_directory['soccer'][0] = 'Andres'
# # print(sports_directory)

# #4. change value 20 in z to 30
# z[0]['x'] = 30
# # print(z)

# 2. Iterate through a list of dictionaries - create a function that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the value
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    for i in range(0, len(students)):
        output = ""
        for key, val in students[i].items():
            output += f"{key} - {val},"
        print(output)

# iterateDictionary(students)

# 3. get value from a list of dictionaries
# def iterateDictionary2(key_name, some_list):
#     for i in range (0, len(some_list)):
#         for key,val in some_list[i].items():
#             if key == key_name:
#                 print(val)

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)


# 4. Iterate through a dictionary with list values - create a function that given a dictionary whose values are all list, prints the name of each key along with the size of the list, and then prints the associated values within each key's list
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printDojo(dictionary):
    for key,val in dictionary.items():
        print()
        print(f"{len(val)} {key.capitalize()}")
        for i in range (0, len(val)):
            print(val[i])

printDojo(dojo)