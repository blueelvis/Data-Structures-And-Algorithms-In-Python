def minmax(data):
  smallest = data[0]
  biggest = data[0]
  for i in data:
    if i > biggest:
       biggest = i
    if i < smallest:
       smallest = i
  return (smallest, biggest)


a = list()
a.append(1)
a.append(100)
a.append(-200)
a.append(-1000)
print(minmax(a))

b = list()
b.append(-1)
b.append(-2.5)
b.append(-34)
print(minmax(b))
