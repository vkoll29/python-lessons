# 1. Simple Decorator without syncatic sugar
"""
def dec_function(func):
    def wrapper():
        from datetime import datetime
        # function only executes if the time is between specified hours
        print(f'The time is {datetime.now()}')
        if 11 <= datetime.now().hour < 23:
            func()
        else:
            print(f"It's too late or too early to do that")
    return wrapper

def scream():
    print('I AM TIRED OF LIFE AS A VIBE')

scream = dec_function(scream)
scream()
"""

# 2. Simple decorator with syntactic sugar
"""
def dec_function(func):
    def wrapper():
        from datetime import datetime
        # function only executes if the time is between specified hours
        print(f'The time is {datetime.now()}')
        if 12 <= datetime.now().hour < 23:
            func()
        else:
            print(f"It's too late or too early to do that")
    return wrapper


@dec_function
def scream():
    print('I AM TIRED OF LIFE AS A VIBE')

# scream()
"""

# 3. Decorating functoins with arguments
# 4. Returning values from decorated functions
"""
def dec_function(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        # function only executes if the time is between specified hours
        print(f'The time is {datetime.now()}')
        if 11 <= datetime.now().hour < 23:
            return func(*args, **kwargs)
        else:
            print(f"Now is a weird time to be shouting, weirdo.")
    return wrapper


@dec_function
def scream(text):
    print('decoration started')
    return(text.upper())

sc = scream("I hate this")
print(sc)
"""

# 5. Type Introspection
# decorated function gets confused about its type. use functools.wraps to avoid this
"""
def dec_function(func):
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        from datetime import datetime
        # function only executes if the time is between specified hours
        print(f'The time is {datetime.now()}')
        if 11 <= datetime.now().hour < 23:
            return func(*args, **kwargs)
        else:
            print(f"Now is a weird time to be shouting, weirdo.")
    return wrapper


@dec_function
def scream(text):
    print('decoration started')
    return(text.upper())

sc = scream("I hate this")
print(scream.__name__)
"""

# 6. Check how long a function takes to execute

def dec_timer(func):
    import functools
    @functools.wraps(func)
    def dec_timer_wrapper(*args, **kwargs):
        from time import perf_counter
        start = perf_counter()
        val =func(*args, **kwargs)
        stop = perf_counter()
        _runtime = stop - start
        print(f"It took {_runtime * 10**3}ms for {func.__name__} to run")
        return val
    return dec_timer_wrapper

# @dec_timer
# def write_file(file_path):
#     with open(file_path, mode='w') as file:
#         file.write("Hello, this was writted from a decorated function")


# write_file('sample.txt')



#trying context managers with decorators
class Write_Read_File:

    def __init__(self, file_path):
        from pathlib import Path
        self.file = Path(file_path)

    def __enter__(self):
        self.file_w = open(self.file, mode='w')
        self.file_r = open(self.file, mode='rb')
        return self

    def __exit__(self, et, ev, etb):
        if self.file_w and self.file_r:
            self.file_w.close()
            self.file_r.close()


# with Write_Read_File('sample1.txt') as file:
#     file.file_w.write("Hi, Can this work?")
#     print(file.file_r.read())



from contextlib import contextmanager
from pathlib import Path

@dec_timer
@contextmanager
def write_read_file(file_path):
    file = Path(file_path)
    file_w = open(file, mode='w')
    file_r = open(file, mode='rb')
    try:
        yield file_w, file_r
    finally:
        file_r.close()
        file_w.close()


# with write_read_file('sample2.txt') as file:
#     file[0].write("Testing if it works")
#     print(file[1].read())



# 7. Debuggin decorator

import functools

def dec_debugger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ', '.join(args_repr+kwargs_repr)
        print(f"calling {func.__name__}({signature})")
        value = func(*args, *kwargs)
        print(f"calling {func.__name__} results in {value!r}")
        return value
    return wrapper


@dec_debugger
def get_exponential(n, e_):
    return n ** e_

# get_exponential(2,3)


# 8. Stateful Decorators with functions
from random import randint, seed
def dec_state(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.num_calls += 1
        # val = func(*args, **kwargs)
        print(wrapper.num_calls)
        return func(*args, **kwargs)
    wrapper.num_calls = 0
    return wrapper

@dec_state
def generate_rand(sd=None):
    if sd:
        seed(sd)
    return randint(0, 10)

# generate_rand(4)


# 9. Stateful Decorators with classes
class CounterDecorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"function {self.func.__name__} has been called {self.num_calls} times")
        return self.func(*args, **kwargs)

@CounterDecorator
def generate_rand(sd=None):
    if sd:
        seed(sd)
    return randint(0, 10)

# generate_rand(4)
# generate_rand(4)
# generate_rand(4)


# 10. Rate Limiting / Slowing down code
import time

# class DecSlowDown:
#     def __init__(self, func=None):
#         @functools.update_wrapper(self, func)
#         self.func = func
#
#     def __call__(self, rate=1, *args, *kwargs):
#         time.sleep(rate)
#         print(f"Slept for {rate} seconds")
#         return self.func(*args, *kwargs)

def slow_down(_func=None, rate=1):
    """Sleep for the specified duration in rate"""
    def dec_slow_down(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(rate)
            print(f'Sleeping for {rate} seconds')
            return func(*args, **kwargs)
        return wrapper

    if _func is None:
        return dec_slow_down()
    else:
        return dec_slow_down(_func)

@dec_timer
@slow_down
def simulate_liftoff(time_left):
    if time_left < 1:
        print("Liftoff")
    else:
        print(time_left)
        simulate_liftoff(time_left-1)

simulate_liftoff(5)
