#(a)
def main():
    print("(a)")
    max = 0
    getMax(1, 2, max)
    print(max)

def getMax(value1, value2, max):
    if value1 > value2:
        max = value1
    else:
        max = value2

main()

#(b)
def main():
    print("(b)")
    i = 1
    while i <= 6:
        print(function1(i, 2))
        i += 1

def function1(i , num):
    line = ""
    for j in range(1, i):
        line += str(num) + ""
        num *= 2
    return line

main()

#(c)
def main():
    print("(c)")
    #times를 초기화한다.
    times = 3
    print("함수 호출 전, 변수 times는", times, "입니다.")

    #nPrint을 호출하고 times를 출력한다.
    nPrint("CS에 오신 것을 환영합니다!", times)
    print("함수 호출 후, 변수 times는", times, "입니다.")

#message를 n번 출력한다.
def nPrint(message, n):
    while n > 0:
        print("n = ", n)
        print(message)
        n -= 1

main()

#(d)
def main():
    print("(d)")
    i = 1
    while i <= 4:
        function1(i)
        i += 1
        print("i는", i, "입니다.")

def function1(i):
    line = " "
    while i >= 1:
        if i % 3 != 0:
            line += str(i) + " "
            i -= 1

    print(line)

main()
