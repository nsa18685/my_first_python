class A:
    def __init__(self, i):
        self.__i = i
    def getI(self):
        return self.__i

def main():
    a = A(5)
    """print(a.__i)"""
    print(a.getI())

main()
