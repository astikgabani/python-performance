"""
set is always the faster than list and tuple while testing for accessing 
"""


import string
import time


char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)


def access_time_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass


print("---------------------------------------")
start = time.perf_counter()
access_time_test(10000000, char_list)
end = time.perf_counter()
print(f"List : {end-start}")

print("---------------------------------------")
start = time.perf_counter()
access_time_test(10000000, char_tuple)
end = time.perf_counter()
print(f"Tuple : {end-start}")

print("---------------------------------------")
start = time.perf_counter()
access_time_test(10000000, char_set)
end = time.perf_counter()
print(f"Set : {end-start}")
print("---------------------------------------")
