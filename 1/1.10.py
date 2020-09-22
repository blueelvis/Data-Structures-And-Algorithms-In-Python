# In order to get a range with values 8,6,4,2,0,-2,-4,-6,-8
# from the range
# constructor, we use the initial, end and step parameters of the
# range function. Do note that the end is not inclusive so we pass
# -10 as the ending value.
# We can also use a negative step.

print(list(range(8, -10, -2)))
