def distinct_odd_product_pair(seq):
  # Ensure that there are only unique elements in the sequence.
  unique_sequence = list(set(seq))

  # Traverse the unique_sequence and find the number of odd numbers
  # since odd * odd = odd, even * even = even, even * odd = even.
  # Also, 0 is neither odd nor even so we will not count it.
  odd_number_count = 0
  for integer in unique_sequence:
    if integer % 2 != 0:
      odd_number_count += 1

  # The number of distinct pairs in this would be (n*n - n)/2
  number_of_distinct_pairs = (odd_number_count * (odd_number_count - 1))/2
  print("Number of distinct pairs whose product is odd - [{0}]".format(int(number_of_distinct_pairs)))
  if number_of_distinct_pairs > 0:
    print(True)
  else:
    print(False)


a = [1,2,3,4,17,66,13,91]

distinct_odd_product_pair(a)

b = [1,1,1,1,1,0,0,0,2]
distinct_odd_product_pair(b)
