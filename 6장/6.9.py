# 최소값 출력하기
def main():
    print(min(5, 6))

def min(n1, n2):
          smallest = n1
          if n2 < smallest:
              smallest = n2

main()

#return값이 없기때문에 None값이 출력된다.
