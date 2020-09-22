def norm(v, p):
  number_list = [i ** p for i in v]
  sum_of_numbers = sum(number_list)
  return sum_of_numbers ** (1 / p)


# In a Euclidean Norm, p == 2
def euclidean_norm(v):
  number_list = [i ** 2 for i in v]
  sum_of_numbers = sum(number_list)
  return sum_of_numbers ** 0.5


v = [4,3]
print("Vector = {0}".format(v))
print("10-norm of the above vector = {0}".format(norm(v,10)))
print("2-norm (Euclidean norm) of the above vector = {0}".format(euclidean_norm(v)))
