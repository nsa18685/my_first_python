#(a)
def function(x):
    print(x)
    x = 4.5
    y = 3.4
    print(y)

x = 2
y = 4

print("(a)")
function(x)
print(x)
print(y)

#(b)
def f(x, y = 1, z = 2):
    return x + y + z

print("(b)")
print(f(1,1,1))
print(f(y = 1, x = 2, z = 3))
print(f(1, z = 3))
