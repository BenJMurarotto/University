def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrone(str):
    stripstr = str.lower().strip()
    print(stripstr[::-1])
    if stripstr == stripstr[::-1]:
        return True
    else:
        return False
    
    
print(is_palindrone('KaPA'))
