# ### Naive Recursive Algo
# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# print(fib(2))


# Memoized Algo
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        f = fib(n-1) + fib(n-2)
        memo[n] = f
        return f

print(fib(9))
