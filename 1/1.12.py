from random import randrange

def choice(sequence):
  random_index = randrange(0, len(sequence),1)
  return sequence[random_index]


a = list()
a.append(1)
a.append(2)
a.append(200)
a.append(-1)
a.append(0)

print(choice(a))
