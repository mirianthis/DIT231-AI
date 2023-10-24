a = ['x', 1, 3.5]
print(a)
print(a[0])

for elt in ["step1", "step2"]:
    print(elt)

#can even put functions and other lists inside of lists!
def f(x):
    return x

b = [f, [1,2,2.1]]
print(b)

a = []
print(a)
for i in range(10):
    a.append(i**2)
    print(a)

while len(a) > 0:
    elt = a.pop()
    print(f"Removed {elt}, a is now {a}")

a = [1,2,3]
a.insert(1,'new value')
print(a)

a = [1.5, 2.5, 3.5, 2.5]
a.remove(2.5)
print(a)

a = [1,2,3]
b = ["x", "y"]
a.extend(b)
print(a)

print(a+b)

print(f"a + [1,2]: {a + [1,2]}")

a = [1.5, 3.5, 2.5]
b = a.copy() # deep
#b = a #shallow
print(f"original a:, {a}")
print(f"original b:, {b}")
b[0] = "edited"
print("after edit...")
print(f"a:, {a}")
print(f"b:, {b}")