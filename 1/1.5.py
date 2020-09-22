def sum_comprehension(n):
  return sum([i**2 for i in range(n)])

print(sum_comprehension(5))
print(sum_comprehension(0))
print(sum_comprehension(100))
