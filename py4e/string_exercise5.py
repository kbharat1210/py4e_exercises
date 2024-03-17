str = 'X-DSPAM-Confidence: 0.8475'
print(str)

s= str.find(':')
print(s)

str = str[s+1:]
print(str)

str = str.strip()
print(str)

str = float(str)
print(str)

