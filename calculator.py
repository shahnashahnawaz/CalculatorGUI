import turtle
import math

# Setup the screen
wn = turtle.Screen()
wn.title("Calculator")
wn.bgcolor("#66545e")
wn.setup(width=400, height=600)

# Global variables
current_input = ""
result = ""

# Function to draw buttons
def draw_button(x, y, width, height, text):
    button = turtle.Turtle()
    button.speed(0)
    button.color("black")
    button.fillcolor("pink")
    button.penup()
    button.goto(x, y)
    button.begin_fill()
    for _ in range(2):
        button.forward(width)
        button.right(90)
        button.forward(height)
        button.right(90)
    button.end_fill()
    button.goto(x + width/2, y - height/2)
    button.write(text, align="center", font=("Arial", 18, "normal"))
    button.hideturtle()
    return button

# Function to draw the display
def draw_display():
    display = turtle.Turtle()
    display.speed(0)
    display.color("pink")
    display.penup()
    display.pensize(5)
    display.goto(-150, 550)
    display.pendown()
    display.forward(500)
    display.right(90)
    display.forward(50)
    display.right(90)
    display.forward(500)
    display.right(90)
    display.forward(50)
    display.hideturtle()

# Update the display with the current input or result
def update_display():
    display_turtle.clear()
    display_turtle.write(current_input if result == "" else result, align="right", font=("Arial", 24, "normal"))

# Function to handle button click
def button_click(x, y):
    global current_input, result
    if -150 < x < -50:
        if 100 < y < 200:
            current_input += "7"
        elif 0 < y < 100:
            current_input += "4"
        elif -100 < y < 0:
            current_input += "1"
        elif -200 < y < -100:
            current_input += "0"
    elif -50 < x < 50:
        if 100 < y < 200:
            current_input += "8"
        elif 0 < y < 100:
            current_input += "5"
        elif -100 < y < 0:
            current_input += "2"
        elif -200 < y < -100:
            current_input += "."
    elif 50 < x < 150:
        if 100 < y < 200:
            current_input += "9"
        elif 0 < y < 100:
            current_input += "6"
        elif -100 < y < 0:
            current_input += "3"
        elif -200 < y < -100:
            current_input = ""
            result = ""
    elif 150 < x < 250:
        if 100 < y < 200:
            current_input += "/"
        elif 0 < y < 100:
            current_input += "*"
        elif -100 < y < 0:
            current_input += "-"
        elif -200 < y < -100:
            current_input += "+"
    elif 250 < x < 350:
        if -200 < y < -100:
            try:
                result = str(eval(current_input))
            except:
                result = "Error"
            current_input = ""
    update_display()

# Draw the display area
draw_display()

# Create display turtle
display_turtle = turtle.Turtle()
display_turtle.speed(0)
display_turtle.color("#f6e0b5")
display_turtle.penup()
display_turtle.goto(130, 220)
display_turtle.hideturtle()

# Draw buttons
buttons = [
    (draw_button(-150, 200, 100, 100, "7"), -150, 100),
    (draw_button(-50, 200, 100, 100, "8"), -50, 100),
    (draw_button(50, 200, 100, 100, "9"), 50, 100),
    (draw_button(150, 200, 100, 100, "/"), 150, 100),
    (draw_button(-150, 100, 100, 100, "4"), -150, 0),
    (draw_button(-50, 100, 100, 100, "5"), -50, 0),
    (draw_button(50, 100, 100, 100, "6"), 50, 0),
    (draw_button(150, 100, 100, 100, "*"), 150, 0),
    (draw_button(-150, 0, 100, 100, "1"), -150, -100),
    (draw_button(-50, 0, 100, 100, "2"), -50, -100),
    (draw_button(50, 0, 100, 100, "3"), 50, -100),
    (draw_button(150, 0, 100, 100, "-"), 150, -100),
    (draw_button(-150, -100, 100, 100, "0"), -150, -200),
    (draw_button(-50, -100, 100, 100, "."), -50, -200),
    (draw_button(50, -100, 100, 100, "C"), 50, -200),
    (draw_button(150, -100, 100, 100, "+"), 150, -200),
    (draw_button(250, 200, 100, 400, "="), 250, -200)
]

# Set up click handler
turtle.onscreenclick(button_click)

# Keep the window open
wn.mainloop()
