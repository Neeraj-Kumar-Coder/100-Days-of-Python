name = input("Enter your name: ")
age = input("Hello {}! Please enter your age: ".format(name.title()))

if (not age.isnumeric()):
    exit("Please enter a valid age!")

age = int(age)
if (age >= 18):
    print("Yes! You can drive")
elif (age >= 13):
    print("You are currently a teenager")
else:
    print("You are a kid right now!")

print("Exiting... Have a nice day ahead!")
