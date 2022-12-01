import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')  #define a cor de fundo

t.hideturtle()
t.goto(0, -10)

#forma o coração
t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(178)
t.end_fill()

#escrita
t.penup()
t.goto(-110, 150)
t.pendown()
t.color('white')
t.write("Eu te amo muito mais", font=("Lucida Calligraphy", 14, "bold"))

t.penup()
t.goto(-110, 130)
t.pendown()
t.color('white')
t.write("que tudo no universo", font=("Lucida Calligraphy", 14, "bold"))

t.penup()
t.goto(-110, 110)
t.pendown()
t.color('white')
t.write("meu Sol <3", font=("Lucida Calligraphy", 14, "bold"))

turtle.done()
