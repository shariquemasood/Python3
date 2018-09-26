def StToList(strings):
	final_data = [b for b in [i.split(' ') for i in strings.split('\n')] if b[0]]
	print (final_data)

StToList("""A B C
D E F
G H I""")
