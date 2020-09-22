def get_number_of_vowels(string):
  number_of_vowels = 0
  for character in string:
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
      number_of_vowels += 1
  return number_of_vowels


a = "hello world!"
b = "aeiou"
c = "yyyzzz"

print("The number of vowels in [{0}] are - {1}".format(a, get_number_of_vowels(a)))
print("The number of vowels in [{0}] are - {1}".format(b, get_number_of_vowels(b)))
print("The number of vowels in [{0}] are - {1}".format(c, get_number_of_vowels(c)))
