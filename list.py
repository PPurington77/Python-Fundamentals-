# fruits = ['apple', 'banana', 'tomato', 'blueberry']
# veggies = ['brocolli', 'potato', 'carrot', 'cucumber']

# fruits_veg = fruits + veggies

# manyFruit = fruits * 5
# print(manyFruit)

# words = ["start","going","till","the","end"]
# # Sub-ranges (portions) of the list
# print(words[1:]) # prints ['going', 'till', 'the', 'end']
# print(words[:4]) # prints ['start', 'going', 'till', 'the']
# print(words[2:4]) # prints ['till', 'the']
# print(words[2:])
    
# # Making a copy of a list
# copy_of_words = words[:]
# copy_of_words.append("dojo") # only appends to the copy
# print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
# print(words) # prints ['start', 'going', 'till', 'the', 'end']
# print(sorted(words))

# some_nums = [44, 56, 2, 3, 12, 19, 6]
# print(some_nums)
# print(len(some_nums))
# some_nums.append(69)
# print(some_nums)
# some_nums.pop()
# print(some_nums)
# list.reverse(some_nums)
# print(some_nums)
# list.sort(some_nums)
# print(some_nums)

# for x in range(0,10,2):
#     print(x)
# for x in range(5,1,-3):
#     print(x)
# for x in range(1, 21):
#     print(x)

# for x in "Patrick":
#     print(x)

# my_list = ["abc", 123, "xyz"]
# for i in range(0, len(my_list)):
#     print(i, my_list[i])
# for v in my_list:
#     print(v)

# countries = ["uganda", "chile", "albania", "saudi arabia"]

# for i in range(0, len(countries)):
#     print("Index:", i)
#     print("Country:", countries[i])

# count = 0
# while count <= 5:
#     print("looping", count)
#     count+=1

y = 3
while y > 0:
    print(y)
    y = y - 1
else: 
    print("final else statement")