a = [1, 2, 3]
b = [4, 5, 6]
print(a)
print(b)
#concatenate
c = a + b
print('Concatenate')
print(c)
#Sliced
t = [9, 41, 12, 3, 74, 15]
print('Sliced')
print(t)
print(t[1:3])
print(t[:4])
print(t[:])
#Build list from scratch
print('Build list from scratch')
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)
#Sort list
print('Sort list')
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
#Slit list
print('Slit list')
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
for w in stuff : print(w)
line = 'first;second;third'
thing = line.split(';')
print(thing)
