def determine_if_distinct(seq):
  if len(seq) == len(set(seq)):
    return True
  else:
    return False


a = [1,1,1,1,1,34,21,5,10]
b = [1,2,34,9,456]

print("Is Sequence A Distinct? {0}".format(determine_if_distinct(a)))
print("Is Sequence B Distinct? {0}".format(determine_if_distinct(b)))
