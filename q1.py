def match(strings):
  cont = 0
  for string in strings:
    if len(string) >= 2 and string[0] == string[-1]:
      cont +=1
  print (cont)

match(['abc', 'ded', 'xyx', 'mno'])
