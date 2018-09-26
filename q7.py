with open('/home/sharique/Python3/SampleTextFile.txt', 'r') as f:
	s = f.read()
	wc={}
	for word in s.split():
		if word not in wc:
			wc[word]=1
		else:
			wc[word]+=1;
	for key,value in wc.items():
		print (key, value)
	maximum = max(wc, key=wc.get)
	print ("Highest Word count is",maximum, wc[maximum])
