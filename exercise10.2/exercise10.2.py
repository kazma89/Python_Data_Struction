count = dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for text in handle :
    if text.startswith('From ') :
        email = text.find(':')
        time = text[email-2:email]
        hours = time.split()

        for h in hours :
            count[h] = count.get(h,0)+1

tmp = list()
for k, v in (count.items()) :
    newtupla = (k, v)
    tmp.append(newtupla)
tmp = sorted(tmp, reverse=False)
for key, val in tmp :
    print(key, val)
