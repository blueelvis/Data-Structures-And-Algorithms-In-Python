def sum_odd_squares(n):
  sum = 0
  for i in range(1,n,2):
    sum += (i ** 2)
  return sum


print(sum_odd_squares(5))
print(sum_odd_squares(100))
