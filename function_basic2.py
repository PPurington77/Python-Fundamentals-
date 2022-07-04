#1. Countdown

# def countDown(num):
#     x = [] #create a variable containing an empty list
#     for i in range(num, -1, -1): #loops i from the argument to 0 in iterations of -1
#         # print(i) #to text if loop is working
#         x.append(i) #pushes i's value to x's list
#     print(x)

# countDown(10)

#2. Print and return
# list = [1, 2] 
# def print_return(list):
#     print(list[0])
#     return list[1]

# x = print_return(list)
# print(x)

#3. first plus length
# list = [16, 2, 3, 4, 5, 6, 7]
# def first_plus_length(list):
#     print(list)
#     sum = list[0] + len(list)
#     print(sum)

# first_plus_length(list)

#4. values greater than second
# list = [4, 5, 6, 9, 1, 2, 1] #variable created so that function can accept array
# def values_greater_than_second(list): #function created
#     newList = [] #variable created so new  list can be created in empty list
#     i = 0 #variable completed for loop
#     while i < len(list): #loops through list
#         if list[i] > list [1]: #if list of i is greater than the 1st index of i then
#             newList.append(list[i]) #add list[i] to newLIst
#         i +=1 
#     # print(newList) #test if this is working..and it is
#     if len(newList) < 3:
#         # print("False") #test if this is working and it is
#         return "False" 
#     else :
#         # print(newList)
#         return newList

# newLists = values_greater_than_second(list)
# print(newLists)

#5. this length, that value 
# def length_and_value(length, value):
#     x = []
#     i = 0
#     while i < length:
#         x.append(value)
#         i +=1
#     # print(x)
#     return x 

# newList = length_and_value(7, 8)
# print(newList)