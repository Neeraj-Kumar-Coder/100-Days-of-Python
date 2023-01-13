my_bio = {
    "name": "Neeraj Kumar",
    "age": 22,
    "gender": "Male",
    "number_of_family_members": 4,
    "hardworker": True
}

print(f"Original: {my_bio}")

my_bio.update({"name": "Bittu"})
print(f"Updated a value: {my_bio}")

my_bio.update({"field_of_study": "Computer Science"})
print(f"Added a field: {my_bio}")

my_bio.pop("hardworker")
print(f"Popped a field: {my_bio}")

my_bio.popitem()
print(f"Popped using popitem(): {my_bio}")

my_bio.clear()
print(f"Dictionary is now empty: {my_bio}")
