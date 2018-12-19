fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	word = line.rstrip().split()
	#print(word)
	for element in word :
		#print(element)
		if element not in lst :
			lst.append(element)
			#print(lst)
		else :
			continue
lst.sort()
print(lst)
