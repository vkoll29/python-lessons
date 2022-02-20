# 1. Simple Decorator without syncatic sugar

def dec_function(func):
    def wrapper():
        from datetime import datetime
        # function only executes if the time is between specified hours
        print(f'The time is {datetime.now()}')
        if 8 <= datetime.now().hour < 23:
            func()
        else:
            print(f"It's too late or too early to do that")
    return wrapper

def scream():
    print('I AM TIRED OF LIFE AS A VIBE')

scream = dec_function(scream)
scream()
