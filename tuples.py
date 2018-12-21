x = ('Gleen', 'Sally', 'Joseph')
print(x[2])
y = (1, 9, 2)
print(y)
print(max(y))
for iter in y :
    print(iter)
print('Sorting lists of tuples by key')
d = {'a':10, 'c':22, 'b':1}
print(d.items())
print(sorted(d.items()))
print('Sorting lists of tuples by value')
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )
print(tmp)
tmp =sorted(tmp, reverse=True)
print(tmp)
