str = 'X-DSPAM-Confidence: 0.8475 '
num = str.rstrip()
#print(len(num))
#print(len(str))
stpos = num.find(' ')
numero = num[stpos+1:]
print(numero)
#print(numero+42.0)
numero = float(numero)
print(numero+42.0)
