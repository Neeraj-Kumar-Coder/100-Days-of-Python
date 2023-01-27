global_variable = 100

print(f"Initially \"global_varible\" has the value = {global_variable}")


def i_will_not_change_global_variable():
    global_variable = 50
    print(
        f"The local variable \"global_variable\" has the value = {global_variable}")


def i_will_change_global_variable():
    global global_variable
    global_variable = 50
    print(
        f"The global variable \"global_variable\" has the value = {global_variable}")


i_will_not_change_global_variable()
print(f"Finally #1: \"global_varible\" has the value = {global_variable}")

i_will_change_global_variable()
print(f"Finally #2: \"global_varible\" has the value = {global_variable}")
