#(1)
a = [ x == False for x in range(100)]
print(a)

#(2)
a.append(5.5)
print(a)

#(3)
print(a[0] + a[1])

#(4)
sum = 0
for i in range(5):
    sum += a[i]
print(sum)

#(5)
print(min(a))

#(6)
import random
j = random.randrange(0, 100)
print(a[j])
