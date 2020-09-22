from random import randint


def shuffle_list(seq):
  for i in range(len(seq)):
    random_int = randint(0,len(seq) - 1) # Since randint is inclusive of both arguments.
    seq[i], seq[random_int] = seq[random_int], seq[i]


a = [1,2,3,4,5,6,7,9,10,11,12,13,14,15]

print("Original List - {0}".format(a))
shuffle_list(a)
print("Shuffled List - {0}".format(a))
shuffle_list(a)
print("Shuffled List - {0}".format(a))

