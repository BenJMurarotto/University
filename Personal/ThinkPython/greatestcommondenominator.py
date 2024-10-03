def gcd(a, b):
    if b == 0:  # Base case: when remainder is zero, gcd is found
        return a
    else:
        return gcd(b, a % b)  # Recursive case: gcd(b, remainder of a % b)



print(gcd(45,15))
