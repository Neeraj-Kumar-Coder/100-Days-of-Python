my_bio = {
    "name": "Neeraj Kumar",
    "age": 22,
    "gender": "Male",
    "number_of_family_members": 4,
    "hardworker": True
}

print(my_bio)
print(my_bio["name"])
print(my_bio["age"])
print(my_bio["gender"])
print(my_bio["number_of_family_members"])
print(my_bio["hardworker"])

# print(my_bio["fjdlkf"])      # throws error (if not present)

# don't throw error (if not present), returns None
print(my_bio.get("fjdljkf"))

print(f"All the keys are: {my_bio.keys()}")
print(f"All the values are: {my_bio.values()}")
print(f"All the pairs are: {my_bio.items()}")

# Iterating
for key in my_bio:
    print(f"{key} -> {my_bio[key]}")

print("".center(30, "*"))
# Another vway
for key, value in my_bio.items():
    print(f"{key} -> {value}")
