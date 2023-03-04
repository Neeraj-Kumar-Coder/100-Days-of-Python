import time


def executeWhile():
    ctr = 0
    while ctr < 100000:
        ctr += 1


def executeFor():
    for ctr in range(100000):
        pass


init = time.perf_counter()
executeWhile()
print(f"This taken by while loop is = {time.perf_counter() - init}")

init = time.perf_counter()
executeFor()
print(f"This taken by for loop is = {time.perf_counter() - init}")
