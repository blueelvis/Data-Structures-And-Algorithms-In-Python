# Typing Ctrl+D on a Linux Terminal causes an EOFError on the terminal

a = []

try:
  while True:
    a.append(input("Please Enter a message - "))
except EOFError as e:
  a.reverse()
  print(a)
