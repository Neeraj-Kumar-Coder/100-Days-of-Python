import threading
import time


def sleeper(seconds):
    time.sleep(seconds)
    print(f"Waked up after {seconds} seconds")
    return seconds


# Normal execution
start = time.perf_counter()

sleeper(4)
sleeper(2)
sleeper(1)

end = time.perf_counter()
print(f"Code runtime without threads = {end - start} seconds")

# Execution with threading
start = time.perf_counter()

thread_1 = threading.Thread(target=sleeper, args=[4])
thread_2 = threading.Thread(target=sleeper, args=[2])
thread_3 = threading.Thread(target=sleeper, args=[1])

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

end = time.perf_counter()
print(f"Code runtime with threads = {end - start} seconds")
