print("***** Welcome to the jarvis calculator *****")
expression = input("Enter your input in the format (a op b): ")

# Validity check (according to 'a op b' rule)
operatorCount = 0
operandCount = 0
haveAlphabet = False
for item in expression:
    if (item == ' '):
        continue

    if (item.isalpha()):
        haveAlphabet = True
        continue

    if (item == '+' or item == '-' or item == '*' or item == '/' or item == '%'):
        operatorCount += 1
    elif (operandCount == 0):
        operandCount += 1
    elif (operandCount == 1):
        operandCount += 1

if (operatorCount > 1 or operatorCount <= 0 or operandCount < 2 or haveAlphabet):
    print("Enter a valid expression! (Hint: negative values are not allowed right now)")
    exit(-1)

number1 = 0
number2 = 0

operator = '\0'
operatorFound = False


for item in expression:
    if (item == ' ' or item.isalpha()):
        continue

    if (item == '+' or item == '-' or item == '*' or item == '/' or item == '%'):
        operator = item
        operatorFound = True
    elif (not operatorFound):
        number1 = number1*10 + int(item)
    else:
        number2 = number2*10 + int(item)

result = -1
if (operator == '+'):
    result = number1 + number2
elif (operator == '-'):
    result = number1 - number2
elif (operator == '*'):
    result = number1 * number2
elif (operator == '/'):
    result = number1 / number2
elif (operator == '%'):
    result = number1 % number2

print("Your Result Is: {}".format(result))
