str1 = "Hello, "
str2 = "World!"
str3 = str1 + str2
print(str3)

x = 23
y = 52
name = "Alice"

str1 = f"{name}'s numbers are {x} and {y}, and their sum is {x + y}"
print(str1)


str1 = "a: %s" % "string"
print(str1)
str2 = "b: %.1f, %s, %d" % (1.0, 'hello', 5)
print(str2)
str3 = "c: {}".format(3.14)
print(str3)


# some methods
str1 = "Hello, World!"
print(str1)
print(str1.upper())
print(str1.lower())

print(dir(str1))

str3 = "Hello, World!"
str3 = str3.lower()
print(str3)

str3 = str3.replace('l', 'p')
print(str3)