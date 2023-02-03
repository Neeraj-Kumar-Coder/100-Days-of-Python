# Snake Water Gun

# P\C    S  W  G
#        0  1  2
#        ________
# S 0 |  0  1 -1
# W 1 | -1  0  1
# G 2 |  1  -1 0

import random

point_matrix = [[0, 1, -1],
                [-1, 0, 1],
                [1, -1, 0]]

if __name__ == "__main__":
    user_points = 0
    name = input("Please enter your good name: ")
    name = name.title()
    print(" Welcome to SNAKE, WATER and GUN game ".center(50, "*"), end="\n\n")
    print("* Instruction: Enter S (snake), W (water) and G (gun)")
    number_of_rounds = random.randint(3, 10)
    print(f"There are total {number_of_rounds} rounds in this match !".center(
        40, "*"), end="\n\n")

    for round in range(1, number_of_rounds + 1):
        print(f"Round {round}")
        user_choice = input("Choose: ")
        user_choice = user_choice.capitalize()
        user_choice = 0 if user_choice == "S" else 1 if user_choice == "W" else 2 if user_choice == "G" else -1
        if (user_choice == -1):
            print("Invalid choice ! CPU got 1 point")
            user_points += -1
            continue

        cpu_choice = random.randint(0, 2)
        print(
            f"CPU's Choice: {'S' if cpu_choice == 0 else 'W' if cpu_choice == 1 else 'G'}")
        user_points += point_matrix[user_choice][cpu_choice]

    if (user_points > 0):
        print(f"Congratulations {name}! You won the match")
    elif (user_points < 0):
        print(f"So sad {name}, You lost !")
    else:
        print(f"That's a tie between {name} and CPU")
