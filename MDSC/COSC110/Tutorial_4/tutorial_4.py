def any_lowercase1(s):
  for c in s:
    if c.islower():
      return True
    else:
      return False


### This function only checks the first character in the string is lowercase or not

def any_lowercase2(s):
  for c in s:
    if 'c'.islower():
      return 'True'
    else:
      return 'False'

### This function doesnt work because it does not check the argument it only checks 'c' which is always lower therefore always returns true
    
def any_lowercase3(s):
  for c in s:
    flag = c.islower()
  return flag

print(any_lowercase3('FLAHg'))

### This function will return whether or not the LAST character in the string is lower or not because flag is changed for each char in s it will return only T or F for the final result

