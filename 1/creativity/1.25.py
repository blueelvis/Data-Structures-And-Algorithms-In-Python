punctuation_list = [".","?","!",",",";",":","-","[","]","(",")","{","}","'","\""]

def remove_punctuations(string):
  string_with_punctuations_removed = ""
  for char in string:
    if char not in punctuation_list:
      string_with_punctuations_removed += char
  return string_with_punctuations_removed

a = "Hello World!"
print("Original String - {0}".format(a))
print("After removing punctuations - {0}".format(remove_punctuations(a)))
