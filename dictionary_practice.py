# person = {"first_name": "Patrick", "last_name": "Purington", "age": 30, "is_organ_donor": True}
# person2 = {"first_name": "Debby", "last_name": "Purington", "age": 52, "is_organ_donor": True}
# # print(person2)

# capitals = {}
# capitals["svk"] = "bratislava"
# capitals["deu"] = "berlin"
# capitals["dnk"] = "copenhagen"
# capitals["usa"] = "washington dc"
# capitals["mex"] = "mexico city"

# print(capitals)

# countries_so_far = {"Mexico": 1, "Morocco": 1}
# new_visits = ["Albania", "Mexico", "Togo", "Morocco"]

# countries_so_far["Albania"] = 1
# countries_so_far["Mexico"] +=1
# countries_so_far["Togo"] = 1
# countries_so_far["Morocco"] +=1
# # print(countries_so_far)
# # print(countries_so_far["Mexico"])
# # del countries_so_far["Togo"]
# # print(countries_so_far)
# for each_key in countries_so_far:
#     print(each_key)
# for each_key in countries_so_far:
#     print(countries_so_far[each_key])

# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}

print(resume_data["skills"][1])
print(users[2]["first"])
