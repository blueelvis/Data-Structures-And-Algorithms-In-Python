def print_dot_product(seq1, seq2):
  print([seq1[i] * seq2[i] for i in range(0,len(seq1))])


a = [1,2,3,4,5,6,7,8,9,10]
b = [10,9,8,7,6,5,4,3,2,1]

print_dot_product(a,b)
