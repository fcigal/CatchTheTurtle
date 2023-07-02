# import libraries
import turtle
import random

# Screen settings
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ('Arial', 30, 'normal')

# Main turtle coordinates and list
x_coordinate = [-20, -10, 0, 10, 20]
y_coordinate = [-20, -10, 0, 10]
turtle_list = []
grid_size = 15
score = 0

# Identify score and countdown turtles
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()

game_over = False


# Score turtle def
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score: 0", move=False, align='center', font=FONT)


# Turtle maker
def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align='center', font=FONT)
        print(x, y)

    t.onclick(handle_click)
    t.color("dark green")
    t.shape("turtle")
    t.penup()
    t.shapesize(2, 2)
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)


# Placing main turtles on defined coordinates
def setup_turtles():
    for x in x_coordinate:
        for y in y_coordinate:
            make_turtle(x, y)


# Hide generated turtles
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


# Recursive function
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)


# Countdown generator
def countdown(time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()
    countdown_turtle.setpos(0, y - 40)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align='center', font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align='center', font=FONT)


# Calling all functions in a start_game function
def start_game():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)


start_game()
turtle.mainloop()
