num = list()
while True:
    inp = input('Enter a number:')
    if inp == 'done' : break
    try :
        num.append(float(inp))
    except :
        print('Bad input')
        continue
print(num)
print(sum(num)/len(num))
