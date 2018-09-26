def sorting(strings):
   list1 = []
   list2 = []
   for string in strings:
       if string.startswith('x'):
          list1.append(string)
       else:
          list2.append(string)
   print (sorted(list1) + sorted(list2))

sorting(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])	
