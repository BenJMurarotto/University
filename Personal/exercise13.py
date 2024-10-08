from math import sqrt
def mysqrt(a):
    x = a + 1
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
        x = y



def printhead():
    head = ['a',   'mysqrt(a)'   'math.sqrt(a)'    'diff'

    ]
    print(head)



def testsquareroot(a):
    printhead()
    body = [a, mysqrt(a), sqrt(a), mysqrt(a) - sqrt(a)]
    print(body)

print(mysqrt(3))
    