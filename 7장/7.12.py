class Count:
    def __init__(self, count = 0):
        self.count = count

def main():
    c = Count()
    n = 1
    m(c, n)

    print("count는", c.count, "입니다.")
    print("n은", n, "입니다.")

def m(c, n):
    c = Count(5) #c.count = 5
    n = 3

main()
