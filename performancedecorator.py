from time import time

def performance(fn):
    def wrapper():
        t1= time()
        result = fn()
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def multiplier():
    for i in range(10000000):
        a=i*5

multiplier()