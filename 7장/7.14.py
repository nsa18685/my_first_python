def main():
    a = A()
    '''a.print()'''
    print(a.getS())

class A:
    def __init__(self, newS = "환영합니다."):
        self.__s = newS

    '''def print(self):
        print(self.__s)'''

    def getS(self):
        return self.__s

main()
