#Is Unique

#Quick solution:

def is_unique(str):
  return len(str) == len(set(str))

#Solved using array:

def is_unique(str):
  array = []
  for letter in str:
    if letter in array:
      return False
  else:
    array.append(letter)
  return True


#Solved using dictionary:
def is_unique(str):
  dict={}
  for letter in str:
    if letter in dict:
      dict[letter]+=1
    else:
      dict[letter]=1
  for val in dict:
    if dict[val]>1:
      return False
    return True
