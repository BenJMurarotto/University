import numbers

def checkfermat(a,b,c,n):

    ans = a**n + b**n
    if ans == c**n:
        print("Holy shit you just solved Fermat's equation!")
        print(f"{ans} is equal to c^n!")
    else:
        print(f"Nawh dog you geeked... {ans} does NOT equal {c**n}")


checkfermat(-1,-1,1,2)



        