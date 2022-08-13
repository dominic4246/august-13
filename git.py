def mostLetter(string):

  most = string[0]
  for i in range(0, len(string)):
    if string.count(most) < string.count(string[i]):
      most = string[i]
  return most
    


print(mostLetter("ccda"))
