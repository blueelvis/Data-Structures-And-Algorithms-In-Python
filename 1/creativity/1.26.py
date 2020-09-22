# Returns True if this condition is satisfied = (a + b = c)
def check_rule1(a,b,c):
  if (a + b) == c:
    return True
  else:
    return False

# Returns True if this condition is satisfied = (a = b - c)
def check_rule2(a,b,c):
  if a == (b - c):
    return True
  else:
    return False

# Returns True if this condition is satisfied = (a * b = c)
def check_rule3(a,b,c):
  if (a * b) == c:
    return True
  else:
    return False

num1 = int(input("Please enter number 1 - "))
num2 = int(input("Please enter number 2 - "))
num3 = int(input("Please enter number 3 - "))

print("Rule (a + b = c) satisfied? {0}".format(check_rule1(num1,num2,num3)))
print("Rule (a = b - c) satisfied? {0}".format(check_rule2(num1,num2,num3)))
print("Rule (a * b = c) satisfied? {0}".format(check_rule3(num1,num2,num3)))

