import multiprocessing as m
import threading as t
from threading import *
import time
# print(m.cpu_count())
# print(t.current_thread().getName())


# def dsp():
#     for i in range(1, 5):
#         print("Child Thread")


# t = Thread(target=dsp)
# t.start()
# for i in range(1, 5):
#     print("Main Thread")

import time  # Import the time module to use sleep and time functions


# def two_power():
#     # This function calculates and prints the powers of 2 from 2^1 to 2^10
#     for n in range(1, 11):
#         time.sleep(1)  # Pause execution for 1 second
#         # Print the result of 2 raised to the power of n
#         print("2 power", n, "is", 2 ** n)


# def five_power():
#     # This function calculates and prints the powers of 5 from 5^1 to 5^10
#     for n in range(1, 11):
#         time.sleep(1)  # Pause execution for 1 second
#         # Print the result of 5 raised to the power of n
#         print("5 power", n, "is", 5 ** n)


# time1 = time.time()  # Record the current time before starting the function

# # Create threads for the two functions
# thread1 = Thread(target=two_power)
# thread2 = Thread(target=five_power)

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for both threads to complete
# thread1.join()
# thread2.join()

# # Print the time elapsed since time1
# print("Time elapsed:", time.time() - time1)
#   ##########################################################


l = Lock()


def wish(name):
    l.acquire()
    for i in range(1, 5):
        print("Good Morning:", end="")
        time.sleep(2)
        print(name)
    l.release()


t1 = Thread(target=wish, args=("Dhoni",))
t2 = Thread(target=wish, args=("Yuvraj",))

t1.start()
t2.start()
