from functools import reduce

# print(reduce((lambda el, acc: el + acc),range(11)))

lst = ['Another', 'word']

print((lambda x: ''.join(x))(lst))