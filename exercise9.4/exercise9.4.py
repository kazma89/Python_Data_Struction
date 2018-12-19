counts = dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle :
    if line.startswith('From '):
        words = line.split()
        email = words[1].split()
        for e in email :
            counts[e] = counts.get(e,0)+1
bigcount = None
bigemail = None
for email,count in counts.items() :
    if bigcount is None or count > bigcount :
        bigemail = email
        bigcount = count
print(bigemail, bigcount)
