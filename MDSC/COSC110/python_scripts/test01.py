def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_leng():
    print('+ - - - -', end=' ')
    

def print_stick():
    print('|        ', end=' ')
    
def print_lengs():
    do_twice(print_leng)
    print('+')

def print_sticks():
    do_twice(print_stick)
    print('|')

def four_sticks():
    do_four(print_sticks)

def stack():
    print_lengs()
    four_sticks()

def two_stack():
    do_twice(stack)

def cube():
    two_stack()
    print_lengs()

cube()


