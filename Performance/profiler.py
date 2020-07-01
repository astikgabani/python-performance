"""
In this script, we are calculating the square of the 1 to 10000000 through different methods.
Using the cProfiler to measure the performance.

::::: Sample Output :::::

----------- Normal Looping -----------
         5 function calls in 3.725 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.725    3.725 <string>:1(<module>)
        1    3.725    3.725    3.725    3.725 profiler.py:15(time_test_normal)
        1    0.000    0.000    3.725    3.725 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


----------- List Comprehension -----------
         5 function calls in 1.812 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.812    1.812 <string>:1(<module>)
        1    0.168    0.168    1.812    1.812 profiler.py:22(time_test_list_comprehension)
        1    1.644    1.644    1.644    1.644 profiler.py:24(<listcomp>)
        1    0.000    0.000    1.812    1.812 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


----------- Lambda Function -----------
         5 function calls in 8.775 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    8.775    8.775 <string>:1(<module>)
        1    0.855    0.855    8.775    8.775 profiler.py:27(time_test_lambda)
        1    7.920    7.920    7.920    7.920 profiler.py:29(<listcomp>)
        1    0.000    0.000    8.775    8.775 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

import cProfile


ls = []
for i in range(10000000):
    ls.append(i)


def time_test_normal():
    global ls
    length = len(ls)
    for i in range(length):
        ls[i] = ls[i] * ls[i]


def time_test_list_comprehension():
    global ls
    [i*i for i in ls]


def time_test_lambda():
    global ls
    [lambda x: x*x for x in ls]


print("----------- Normal Looping -----------")
profiler = cProfile.Profile()
profiler.run("time_test_normal()")
profiler.print_stats()

profiler.clear()

print("----------- List Comprehension -----------")
profiler.run("time_test_list_comprehension()")
profiler.print_stats()

profiler.clear()

print("----------- Lambda Function -----------")
profiler.run("time_test_lambda()")
profiler.print_stats()
