import math
S = [math.sqrt(x) for x in range(21) if x % 3 == 0]
print(S)

S= []
for x in range(21):
    if x % 3 == 0:
        S += [math.sqrt(x)]
print(S)

S = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            if (i + j + k)%2 == 0:
                S += [(i,j,k)]

print(S)

# you aren't restricted to a single for loop
S = [(i,j,k) for i in range(2) for j in range(2) for k in range(2) if (i + j + k)%2 == 0]
print(S)
