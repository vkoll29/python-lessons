"""
# 1. lambda as a higher order func
higher_order_func = lambda x, func: x + func(x)
higher_order_func(3, lambda x: x * x)

# applying decorators to lambdas
def trace(f):
    def wrap(*args, **kwargs):
        print(f"TRACE: func_name: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)
    return wrap

# 2. apply the decorator above to a normal func
@trace
def add_numbers(a, b):
    return a + b

add_numbers(4, 7)

# apply to lambda
print((trace(lambda a,b: a+b))(4,7))


# 3. Closures and Lambdas

def outer_func(x):
    y = 4
    def inner_func(z):
        print(f'x: {x}, y: {y}, z: {z}')
        return x + y + z
    return inner_func

for i in range(3):
    closure = outer_func(i)
    print(f'closure({i+5}): {closure(i+5)}')


# same function with lambda
def outer_func_l(x):
    y = 4
    return lambda z: x+y+z

for i in range(2, 5):
    # closure = outer_func_l(i)
    inner = outer_func_l(i)(i+5)
    print(f'inner({i+5}): {inner}')
"""

# 4. Testing Lambda funcs

# using unittest
import unittest

add_two_numbers = lambda a, b: a+b

class LambdaTest(unittest.TestCase):
    def test_add_two_and_seven(self):
        self.assertEqual(add_two_numbers(2, 7), 9)

    def test_add_three_neg_three(self):
        self.assertEqual(add_two_numbers(3, -3), 0)

    def test_add_five_point_1_four(self):
        # should fail
        self.assertEqual(add_two_numbers(5.1, 4), 9)


# using doctest
add_two_numbers.__doc__ = """ add the two arguments
    >>> add_two_numbers(2,7)
    9
    >>> add_two_numbers(3,-3)
    0
    >>> add_two_numbers(5.1, 4)
    9
    """

if __name__ == '__main__':
    # unittest.main(verbosity=2) # uncomment this to use unittest
    import doctest
    doctest.testmod(verbose=True)