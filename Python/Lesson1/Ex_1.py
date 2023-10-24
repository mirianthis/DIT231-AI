i = 0
j = 2**i

while j < 10000:

    print(j)
    j = 2 ** i
    i = i + 1

def myFunc(a,b):
    return a+2*b

print(myFunc(2,1))

def secFunc(n):
    num1 = 0
    num2 = 1

    if n>0:
        print(num1)
    if n>1:
        print(num2)

    sum = num1 + num2
    while sum<n:
        print(sum)
        num1 = num2
        num2 = sum
        sum =num1 + num2


print(secFunc(10000))






