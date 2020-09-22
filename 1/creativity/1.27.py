def factors(n): # generator that computes factors
  k = 1
  temp_list = []
  while k * k < n: # while k < sqrt(n)
    if n % k == 0:
      yield k
      temp_list.append(n // k)
    k += 1
  if k * k == n: # special case if n is perfect square
    yield k
  for value in reversed(temp_list):
    yield value

num = int(input("Please Enter a Number to find factors - "))

factor_list = []
for factor in factors(num):
  factor_list.append(factor)

print(factor_list)

