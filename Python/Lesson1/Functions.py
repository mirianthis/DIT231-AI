# def tells python you're trying to declare a function
def triangle_area(base, height):
    #here are operations
    #part of function
    #etc
    return 0.5 * base * height

print(triangle_area(1, 2))

def simple(a,b):
    return a,b

# everything in python is an object, and can be passed into a function
def f(x):
    return x+2

def twice(g,x):
    return g(g(x))

twice(f,2) # + 4

def simple(a):
    return (a,a+1,a+2,a+3)

a,b,c,d = simple(1)
print(a)
print(b)
print(c)
print(d)

def n_apply(f, x, n):
    """applies f to x n times"""
    for _ in range(n):  # _ is dummy variable in iteration
        x = f(x)
    return x

n_apply(f, 1, 5) # 1 + 2*5

def g(a, x, b=0):
    return a * x + b

def h(a, b, x=3,y=2):
    return a * x + b*y

h(1,1,y=1) #equivalent to h(1,1,3,1)

g(2, 5, 1)

g(2, 5)