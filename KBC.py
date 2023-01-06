import time

title = "Welcome to Kaun Banega Crorepati (KBC)"
print(title.center(70, "*"))
time.sleep(1)
print("Let's Play!!!".center(70, "*"))
time.sleep(1)
prize_pools = [1000, 2000, 5000, 10000, 25000, 150000,
               320000, 1250000, 2500000, 5000000, 100000000]

prize_pools.reverse()
print(" Prize Pool ".center(30, "#"))
for amount in prize_pools:
    print("₹ {}".format(amount))
prize_pools.reverse()

questions = [
    {
        "question": "Who is the father of Computers?",
        "option_1": "James Gosling",
        "option_2": "Charles Babbage",
        "option_3": "Dennis Ritchie",
        "option_4": "Bjarne Stroustrup",
        "correct_answer": 2
    },
    {
        "question": "Which of the following is the correct abbreviation of COMPUTER?",
        "option_1": "Commonly Occupied Machines Used in Technical and Educational Research",
        "option_2": "Commonly Operated Machines Used in Technical and Environmental Research",
        "option_3": "Commonly Oriented Machines Used in Technical and Educational Research",
        "option_4": "Commonly Operated Machines Used in Technical and Educational Research",
        "correct_answer": 4
    },
    {
        "question": "Which of the following is the correct definition of Computer?",
        "option_1": "Computer is a machine or device that can be programmed to perform arithmetical or logic operation sequences automatically",
        "option_2": "Computer understands only binary language which is written in the form of 0s & 1s",
        "option_3": "Computer is a programmable electronic device that stores, retrieves, and processes the data",
        "option_4": "All of the mentioned",
        "correct_answer": 4
    },
    {
        "question": "What is the full form of CPU?",
        "option_1": "Computer Processing Unit",
        "option_2": "Computer Principle Unit",
        "option_3": "Central Processing Unit",
        "option_4": "Control Processing Unit",
        "correct_answer": 3
    },
    {
        "question": "Which of the following language does the computer understand?",
        "option_1": "Computer understands only C Language",
        "option_2": "Computer understands only Assembly Language",
        "option_3": "Computer understands only Binary Language",
        "option_4": "Computer understands only BASIC",
        "correct_answer": 3
    },
    {
        "question": "Which of the following computer language is written in binary codes only?",
        "option_1": "pascal",
        "option_2": "machine language",
        "option_3": "C",
        "option_4": "C#",
        "correct_answer": 2
    },
    {
        "question": "Which of the following is the brain of the computer?",
        "option_1": "Central Processing Unit",
        "option_2": "Memory",
        "option_3": "Arithmetic and Logic unit",
        "option_4": "Control Unit",
        "correct_answer": 1
    },
    {
        "question": "Which of the following is not a characteristic of a computer?",
        "option_1": "Versatility",
        "option_2": "Accuracy",
        "option_3": "Diligence",
        "option_4": "I.Q.",
        "correct_answer": 4
    },
    {
        "question": "Which of the following is the smallest unit of data in a computer?",
        "option_1": "Bit",
        "option_2": "Byte",
        "option_3": "Nibble",
        "option_4": "Kilo Byte",
        "correct_answer": 1
    },
    {
        "question": "Which of the following unit is responsible for converting the data received from the user into a computer understandable format?",
        "option_1": "Output Unit",
        "option_2": "Input Unit",
        "option_3": "Memory Unit",
        "option_4": "Arithmetic and Logic Unit",
        "correct_answer": 2
    },
    {
        "question": "Which of the following is not a type of computer code?",
        "option_1": "EDIC",
        "option_2": "ASCII",
        "option_3": "BCD",
        "option_4": "EBCDIC",
        "correct_answer": 1
    }
]

on_pool = 0
number_of_pools = len(prize_pools)
while (on_pool < number_of_pools):
    print("Question number {} for ₹ {} on your screen now!".format(
        on_pool + 1, prize_pools[on_pool]))
    time.sleep(2)
    print("Q{}. {}".format(on_pool + 1, questions[on_pool]["question"]))
    time.sleep(3)
    print("A. {}\nB. {}\nC. {}\n D. {}".format(
        questions[on_pool]["option_1"], questions[on_pool]["option_2"], questions[on_pool]["option_3"], questions[on_pool]["option_4"]))
    chosen_option = input("Enter the correct answer: ")
    if (not chosen_option.isnumeric()):
        exit("Please enter a valid option!")
    chosen_option = int(chosen_option)
    time.sleep(3)
    if (chosen_option == questions[on_pool]["correct_answer"]):
        print("Congratulations!! You got the correct answer and won ₹ {}".format(
            prize_pools[on_pool]))
        on_pool += 1
    else:
        print("Sorry! That's the wrong answer")
        break

time.sleep(1)
print("Congratulations!! You won ₹ {}".format(
    prize_pools[min(on_pool, number_of_pools - 1)]))
time.sleep(1)
print("Money Successfully got credited to your bank account!!")
