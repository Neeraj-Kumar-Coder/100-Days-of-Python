targets = list()

while (target := input("Enter your target: ")) != "till now":
    targets.append(target)

print(f"Your targets are:")

for index, target in enumerate(targets):
    print(f"{index}. {target}")
