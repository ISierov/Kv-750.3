"""
Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array (true means present).
"""
def count_sheeps(sheeps):
    lst = list(sheeps)

    return sum(list(x for x in lst if x ))

print(count_sheeps([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  None,  True ,
  False, False, True,  True]))


