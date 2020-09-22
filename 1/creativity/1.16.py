# The reason this happens because the data is an alias to the
# original parameter passed to the function. Since we are not
# doing any change to the whole object itself, this works.
# For example, if we were to do something like data = [],
# that would break the alias.

def scale(data, factor):
  for j in range(len(data)):
    data[j] *= factor


a = [1,2,3,4,5,6,7,8,9,10]

print("Original Sequence - {0}".format(a))
scale(a, 10)
print("Modified Sequence - {0}".format(a))
