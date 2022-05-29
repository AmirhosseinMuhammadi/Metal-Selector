import turtle
from KNN import *
turtle.ht()
turtle.speed(0)
turtle.title("Metal Detector")

def write_text(x , y , size , c , text):
    turtle.pu()
    turtle.goto(x , y)
    turtle.pd()
    turtle.color(c)
    style = ("b tabassom" , size , "bold italic")
    turtle.write(text , font = style , align = "center")

def function(a):
    bgpic = f"ezgif-1-0e84d0860a-gif-im/frame_{a}_delay-0.03s.gif"
    win = turtle.Screen()
    win.addshape(bgpic)
    sh = turtle.Turtle()
    sh.shape(bgpic)

for i in range(50):
    function(i)

def rectangle(x , y , c , w , h):
    turtle.pu()
    turtle.goto(x , y)
    turtle.pd()
    turtle.color(c)
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(w)
        turtle.lt(90)
        turtle.fd(h)
        turtle.lt(90)
    turtle.end_fill()


rectangle(-500 , -500 , "tomato" , 1000 , 1000)
turtle.bgcolor("tomato")
rectangle(-150 , 37.5 , "limegreen" , 300 , 75)
rectangle(-100 , -25 , "limegreen" , 200 , 50)
write_text(0 , 50 , 36 , "red" , "Start")
write_text(0 , -12.5 , 24 , "red" , "Exit")

def clicked(x , y): 
    if x > -150 and x < 150:
        if y > 37.5 and y < 107.5:
            yieldStrength = turtle.numinput("InputBox" , "Enter Yield Strength(ksi) : ")
            density = turtle.numinput("InputBox" , "Enter Density(lb/in^3) : ")
            price = turtle.textinput("InputBox" , "Enter Price Range(USD/Kg) : ")
            price = price.split("-")
            price = (float(price[0]) * 1000 + float(price[1]) * 1000) / 2
            a = [[yieldStrength , density , price]]
            test = pd.DataFrame(a)
            result , neigh = knn(df , test , 3)
            #turtle.clear()
            rectangle(-500 , -500 , "tomato" , 1000 , 1000)
            write_text(0 , 0 , 36 , "khaki" , result)
            turtle.listen()

    if x > -100 and x < 100:
        if y > -25 and y < 25:
            turtle.bye()


turtle.onscreenclick(clicked)
turtle.listen()
turtle.mainloop()