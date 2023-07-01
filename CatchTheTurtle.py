import turtle
import random

# Turtle and screen settings
catch_turtle = turtle.Screen()
catch_turtle.bgcolor("light blue")
catch_turtle.title("Python Turtle Graphics")
turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("Green")
turtle_instance.shapesize(2, 2, 2)
turtle_instance.penup()
font = ("Arial", 30, "normal")
score = 0
timer = 20
timer_up = False

score_writer = turtle.Turtle()
counter = turtle.Turtle()




def countdown():
    counter.hideturtle()
    score_writer.hideturtle()
    counter.penup()
    score_writer.penup()
    counter.setposition(-40, 300)
    score_writer.setposition(-40, 350)
    global timer, timer_up, score
    score_writer.clear()
    counter.clear()
    if timer == 20:
        counter.color("black")
        score_writer.color("blue")
        print('\033[32m'"")
    if timer <= 0:
        counter.write("Time is up", font=font)
        score_writer.write("Score: ", font=font)
        print('\033[31m'"Time's Up")
        timer_up = True
    else:
        counter.write("Time: " + str(timer), font=font)
        timer -= 1
        counter.getscreen().ontimer(countdown, 1000)
        catch_turtle.ontimer(turtle_animate, 300)
    score_writer.write("Score: " + str(score), font=font)




def turtle_animate():
    turtle_instance.goto(random.randint(-300, 0), random.randint(0, 300))


def add_score(x, y):
    global score
    score += 1
    print(score)
    turtle_animate()


turtle_instance.onclick(add_score)
catch_turtle.ontimer(countdown, 1000)
catch_turtle.mainloop()
