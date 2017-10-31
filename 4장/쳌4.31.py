# 조건식으로 if문

x, y, z = eval(input("세 수를 입력하세요. ex) 2, 3, 6: "))
print("정렬되어 있음" if x < y and y < z else "정렬되어 있지 않음")

#if문으로 변형
#if x < y and y < z:
#    print("정렬되어 있음")
#else:
#    print("정렬되어 있지 않음")
