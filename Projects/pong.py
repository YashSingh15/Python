import turtle

# Screen Dimensions

width = 800
height = 600

xLeft = -width / 2
xRight = width / 2

yUp = height / 2
yDown = -height / 2

# Setup

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=width, height=height)
wn.tracer(0)

# Score

score_a = 0
score_b = 0

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, height / 2 - 40)
pen.write(f"Player A: {score_a}, Score B: {score_b}", align="center", font=("Courier", 24, "normal"))

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a_x = xLeft + 50
paddle_a.goto(paddle_a_x, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b_x = xRight - 50
paddle_b.goto(paddle_b_x, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.8 * (width / 800)
ball.dy = 0.8 * (height / 600)


# Movement Functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 * (height / 600)
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 * (height / 600)
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20 * (height / 600)
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 * (height / 600)
    paddle_b.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Game

while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() >= height / 2:
        ball.sety(height / 2)
        ball.dy = -ball.dy

    if ball.ycor() <= -height / 2:
        ball.sety(-height / 2)
        ball.dy = -ball.dy

    if ball.xcor() >= width / 2:    # A scores
        ball.setx(0)
        ball.sety(0)
        ball.dx = -ball.dx
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}, Score B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() <= -width / 2:   # B scores
        ball.setx(0)
        ball.sety(0)
        ball.dx = -ball.dx
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}, Score B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Ball collides with paddle

    if (paddle_b.xcor() - 10 <= ball.xcor() <= paddle_b.xcor()) and (
            paddle_b.ycor() - 50 <= ball.ycor() <= paddle_b.ycor() + 50):
        ball.dx = -ball.dx

    if (paddle_a.xcor() <= ball.xcor() <= paddle_a.xcor() + 10) and (
            paddle_a.ycor() - 50 <= ball.ycor() <= paddle_a.ycor() + 50):
        ball.dx = -ball.dx

    # Set bounds for paddles

    if paddle_b.ycor() + 50 >= height / 2:
        paddle_b.goto(width / 2 - 50, height / 2 - 50)

    if paddle_b.ycor() - 50 <= -height / 2:
        paddle_b.goto(width / 2 - 50, -height / 2 + 50)

    if paddle_a.ycor() + 50 >= height / 2:
        paddle_a.goto(-width / 2 + 50, height / 2 - 50)

    if paddle_a.ycor() - 50 <= -height / 2:
        paddle_a.goto(-width / 2 + 50, -height / 2 + 50)
