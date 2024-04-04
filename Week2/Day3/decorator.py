#Decorators

#Syntax: How to apply the decorator
#@nameoffunction
#def do_this():
    #pass

#Syntax 2

import time

def tictoc(func): # the decorator function
    def wrapper():
        t1 = time.time() # 11:50:03:5
        func() # function called, executed and returned
        total = time.time() - t1 #11:50:06:5 - 11:50:03:5 = 03:0
        print(f"{func.__name__}Took {total} seconds")
    return wrapper
        # code to calculate the execution time

@tictoc
def do_this():
    #code of the func
    time.sleep(2)

@tictoc
def do_that():
    time.sleep(1.5)

@tictoc
def do_something():
    time.sleep(0.5)

do_this()
do_that()
do_something()
print('Finished')