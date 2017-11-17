# 최소값 출력하기2
def main():
    print(min(min(5, 6), (51, 6)))

def min(n1, n2):
          smallest = n1
          if n2 < smallest:
              smallest = n2

main()
#TypeError: '<' not supported between instances of 'tuple' and 'NoneType'
#NonType:return문이 없기 때문
