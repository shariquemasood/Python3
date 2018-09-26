import numpy as np
def StToList(strings):
	string2 = strings.replace(" ","")
#	print (type(string2))
	oldList = (string2.split("\n"))
#	print (type(oldList))
	print (oldList)
	newList = [','.join(a).split(" ") for a in oldList]
	newList1 = [''.join(a).replace("'","") for a in newList]
#	print ('[%s]' % ', '.join(map(str, newList1)))
#	print (type(newList))
	print (str(newList))

	print (str(newList1))
#	s = ",".join(str(newList)).replace(",", " ")
#	print (s)
	print ([''.join(a).replace("'","") for a in newList])
#	results = [int(i) for i in newList]
#	print (results)
#	result = np.array(list(oldList))
	print (result)
#	B = np.reshape(result, (-1, 2))
#	print (B)
#	lst = [[a] for a in result]
#	print (lst)

StToList("""A B C
D E F
G H I""") 
