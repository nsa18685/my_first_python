score = eval(input("Input your score: "))
pay = eval(input("Input your pay: "))

if score > 90:
    afterPay = pay * (1 + 0.03)
else:
    afterPay = pay * (1 + 0.01)
print("afterPay: ",afterPay)
    
