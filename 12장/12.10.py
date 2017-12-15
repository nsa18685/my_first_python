class A:
    def __new__(self):
        self.__init__(self)
        print("A의 __new__()가 호출됨")
    def __init__(self):
        print("A의 __init__()가 호출됨")

class B(A):
    def __new__(self):
        self.__init__(self)
        print("B의 __new__()가 호출됨")
    def __init__(self):
        print("B의 __init__()가 호출됨")

def main():
    b = B()
    a = A()
main()
