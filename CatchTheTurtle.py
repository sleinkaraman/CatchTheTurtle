import turtle
import random

screen=turtle.Screen()
screen.bgcolor("light gray")

score=0
FONT=("Arial",30,"bold")
gridSize=10
gameOver=False

turtleList=[]

scoreTurtle=turtle.Turtle()

def setupScore():
    scoreTurtle.hideturtle()
    scoreTurtle.penup()
    height=turtle.window_height()
    y=height*0.35

    scoreTurtle.setpos(0,y)
    scoreTurtle.color("black")
    scoreTurtle.write(arg="Score: 0", move=False, align="center", font=FONT)

def makeTurtle(x,y):
    t=turtle.Turtle()
    t.penup()

    def click(x,y):
        global score
        score+=1
        scoreTurtle.clear()
        scoreTurtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    t.onclick(click)
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.setpos(x*gridSize,y*gridSize)

    turtleList.append(t)

x_co=[-20,-10,0,10,20]
y_co=[-20,-10,0,10,20]

def setupTurtles():
    for x in x_co:
        for y in y_co:
            makeTurtle(x,y)

def hideTurtles():
    for t in turtleList:
        t.hideturtle()
def showTurtles():
    if not gameOver:
        hideTurtles()
        random.choice(turtleList).showturtle()
        screen.ontimer(showTurtles,500)
        
countdownTurtle=turtle.Turtle()
def countdown(time):
    global gameOver
    countdownTurtle.hideturtle()
    countdownTurtle.penup()
    height = turtle.window_height()
    y = height * 0.42

    countdownTurtle.setpos(0, y)
    countdownTurtle.color("black")
    countdownTurtle.clear()

    if time>0:
        countdownTurtle.clear()
        countdownTurtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time-1),1000)
    else:
        gameOver=True
        countdownTurtle.clear()
        hideTurtles()
        countdownTurtle.write(arg="Game Over!", move=False, align="center", font=FONT)







turtle.tracer(0)
setupScore()
setupTurtles()
hideTurtles()
showTurtles()
countdown(10)
turtle.tracer(1)




turtle.mainloop()
