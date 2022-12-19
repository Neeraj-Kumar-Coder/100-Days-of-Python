# There are two types of typecasting

# Explicit typecasting
a = "12"
b = "98"

print("Before typecasting {} + {} = {} (The type is: {})".format(a, b, a+b, type(a + b)))
print("After typecasting {} + {} = {} (The type is: {})".format(int(a),
      int(b), int(a) + int(b), type(int(a) + int(b))))

# Implicit typecasting
a = 9.3
b = 1

print("This is automatic (or implicit) typecasting: {} + {} = {} (The type is: {})".format(a, b, a+b, type(a + b)))
