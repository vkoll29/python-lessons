def scope_test():
    def do_local():
        spam = "local spam"
        print(spam)

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        print(spam)

    def do_global():
        global spam
        spam = "global spam"
        print(spam)

    spam = "test spam"
    do_local()
    print(f'After local assignment: {spam}')
    do_nonlocal()
    print(f'After nonlocal assignment: {spam}')
    do_global()
    print(f'After global assignment: {spam}')

scope_test()
print(f'Spam in global scope: {spam}')
