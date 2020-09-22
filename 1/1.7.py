def sum_odd_comprehension(n):
  return sum([i**2 for i in range(1,n,2)])


print(sum_odd_comprehension(5))
print(sum_odd_comprehension(10))
