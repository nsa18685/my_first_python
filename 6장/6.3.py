def max(num1, num2):
    result = num1 if (num1 > num2) else num2
    return result

def main():
    i = 5
    j = 2
    k = max(i, j)
    print(i,"와/과", j, "중에서 큰 수는", k, "입니다.")

main()
