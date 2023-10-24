a = ['a', 'b', 'c']
a.insert(1, 'd')
print(a)
a.remove('b')
print(a)

X = [i for i in range(100)]

print(X)

s1 = [x for x in X if x%5 == 2]
print(s1)

s2 = [x for x in s1 if x%2 == 0]
print(s2)

s3 = {(x,y) for x in s1 for y in s2}
print(s3)