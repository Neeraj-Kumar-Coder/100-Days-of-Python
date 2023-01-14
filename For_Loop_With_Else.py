for count in range(0, 10):
    print(f"The count now is ==> {count}")
else:
    print(f"Loop ended normally!")

for count in range(0, 5):
    print(f"The count is => {count}")
    if (count == 3):
        break
else:
    print(f"I will never be executed")
