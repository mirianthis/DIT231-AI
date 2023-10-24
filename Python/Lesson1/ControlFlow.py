x = 3
y = 2
z = 1
if x == y:
    print("Hello")
elif x == z:
    print("Goodbye")
elif x == 3:
    print("x is 3")
else:
    print("???")


if 1 == 2:
    print("this runs")
print("this runs too")

print("loop 1")
for i in range(5): # default - start at 0, increment by 1
    print(i)

print("\nloop 2")
for i in range(10, 2, -2): # inputs are start, stop, step
  print(i)

i = 1
while i < 100:
    print(i**2)
    i += i**2  # a += b is short for a = a + b

for num in range(2, 10):
    if num % 2 == 0:
        continue # this jumps us back to the top
    print(f"Found {num}, an odd number")

n = 64
for x in range(2, n):
    if n % x == 0: # if n divisible by x
        print(f'{n} equals {x} * {n // x}')
        break

for i in range(5):
    print(f"i = {i}")
    # print("i = %d" % (i))
    for j in range(5*i):
        if j == 10:
            print(j)
            break
    #break exits to here

if False:
    pass #do nothing
else:
    print('True!')