# break와 continue
print('(a)')

balance = 1000
while True:
    if balance < 9:
        break
    balance = balance - 9
	
print("잔액은", balance, "원 입니다.")


print('(b)')

balance = 1000
while True:
    if balance < 9:
        continue
    balance = balance - 9
	
print("잔액은", balance, "원 입니다.")
