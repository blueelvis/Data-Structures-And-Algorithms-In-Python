# The reason this doesn't modify the original list because in the for
# loop we just are taking the value out of the data sequence. The val
# parameter has a separate reference.

def scale(data, factor):
  for val in data:
    val *= factor


a = [1,2,3,4,5]

print("Original Sequence = {0}".format(a))
scale(a, 10)
print("Even after calling the function, sequence is = {0}".format(a))
