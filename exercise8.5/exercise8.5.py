count = 0
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
for line in fh :
    if line.startswith('From ') :
        word = line.rstrip()
        email = word.split()
        print(email[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
