# Python 3.6 onwards (f-strings)

letter = "Hello I am {}. I am {} years old and currently living in {}"
name = "Neeraj"
age = 22
country = "India"

print(letter.format(name, age, country))

# Including the arguments number
letter = "Hello I am {2}. I am {0} years old and currently living in {1}"
print(letter.format(age, country, name))

# Including mapping
letter = "Hello I am {name}. I am {age} years old and currently living in {country}"
print(letter.format(age=age, name=name, country=country))

# *********Using f-strings*********
print(
    f"Hello I am {name}. I am {age} years old and currently living in {country}")

price = 34.2346
print(f"The price is {price:.3f}")

# Displaying f-string as it as
print(
    f"Hello I am {{name}}. I am {{age}} years old and currently living in {{country}}")
