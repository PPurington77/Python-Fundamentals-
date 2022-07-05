#1. Countdown - create a function that accepts a number as an input. Return a new list that counts down by one, from the number, down to 0
# numList = []
# def countdown(num1):
#     for i in range(num1, 0, -1):
#         # print(i)
#         numList.append(i)
#     return numList

# # countdown(10)
# print(numList)

#2. Print and return - create a function that will receive a list with two number. Print the first value and return the second

# def printReturn(list):
#     print(list[0])
#     return (list[1])

# print(printReturn([2,3]))

#3. First plus length - create a function that accepts a list and returns the sum of the first value in the list plus the lists length
# def firstPlusLength(list):
#     sum = list[0] + len(list)
#     return sum 

# print(firstPlusLength([1, 2, 4, 5, 6, 9]))

#4. Values greater than second - write a function that accepts a list and creates a new list containing only the value from the original list that are greater than its 2nd value. print how many values this is and the return the new list. if the list has less than 2 elements have the function return false
# def valueGreater(listNum):
#     newList = []
#     if len(listNum) < 2:
#         return False
#     for i in range(0, len(listNum)):
#         if listNum[i] > listNum[1]:
#             newList.append(listNum[i])
#     print(newList)
    
# print(valueGreater([10]))

#5. This length, that value - write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose value are all the given value
def lengthValue(size, value):
    returnList = []
    for i in range(0, size):
        returnList.append(value)
    print(returnList)
    return returnList

lengthValue(7, 8)