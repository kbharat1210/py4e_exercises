def chop(s:list):
    del s[0]
    del s[-1]

t = ([1,2,3,4])
chop(t)
print(t)