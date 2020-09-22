def squares(n):
  n = n-1
  sum = 0
  while n > 0:
    sum += (n**2)
    n -= 1
  return sum

print(squares(2))
print(squares(0))
print(squares(100))
