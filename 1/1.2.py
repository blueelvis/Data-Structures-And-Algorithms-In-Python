def is_even(k):
  while k > 0 :
    k -= 2
  if k == 0:
    return True
  else:
    return False


print(is_even(10))
print(is_even(15))
print(is_even(13))
