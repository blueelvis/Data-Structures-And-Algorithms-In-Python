# Use in place reversing.

def reverse_list(sequence):
  reversed_list = sequence
  #for i in range(len(sequence) - 1,-1, -1):
  # reverse
  reversed_list[0] = "abcd"
  return reversed_list


a = list()
a.append(-1)
a.append(-200)
a.append(0)
a.append(100231)


print("List before reversing - {0}".format(a))
print("List after reversing - {0}".format(reverse_list(a)))
