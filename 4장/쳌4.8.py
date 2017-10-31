score = eval(input("Input your score: "))
pay = eval(input("Input your pay: "))

if score > 90:
    afterPay = pay * (1 + 0.03)
    print("afterPay: ",afterPay)
