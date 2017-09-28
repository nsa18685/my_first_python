#한 선을 잇는 두 점의 좌표 구하기 

import turtle

a= -39
b= 48

c= 50
d= -50

turtle.color("red")
turtle.penup()
turtle.goto(a, b)
turtle.pendown()
turtle.goto(c, d)

print((a , b) , (c , d))
