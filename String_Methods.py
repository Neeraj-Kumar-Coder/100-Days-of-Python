"Strings are immutable"

sample = "This is a sample string"
print(sample.upper())
print(sample.lower())

dumbo = "     this is something alternating    !!!!!!"
print(dumbo)
print(dumbo.strip())
print(dumbo.rstrip("!"))
print(dumbo.replace("is", "will be"))
print(dumbo.split(" "))
print(dumbo.strip().rstrip("!").capitalize().strip())

heading = "Welcome to the future"
print(heading.center(50, "*"))
print(heading.find("me"))
heading += '\n'  # '\n' is not printable
print(heading.isprintable())
print(heading.isspace())
print(heading.istitle())

title = "This Is Title"
print(title.istitle())
print(title.swapcase())

notTitle = "this is originally not a title"
print(notTitle.title())
