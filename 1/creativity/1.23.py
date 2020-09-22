a = [1,2,3,4]

try:
  for i in range(1,11):
    print(a[i])
except IndexError as e:
  print("Don't try buffer overflow attacks in Python!")
