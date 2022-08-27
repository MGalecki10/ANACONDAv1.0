import turtle
import random
import time

#Game_parameters
GAME_HEIGHT = 900
GAME_WIDTH = 900
SPACE_SIZE = 50
BACKGROUND_COLOR = "#c2f7f7"
SNAKE_COLOR = "purple"
FOOD_COLOR = "red"
SNAKE_SHAPE = "square"
BODY_COLOR = "green"
FOOD_SIZE = "circle"
delay = 0.1

window = turtle.Screen()
window.title("Snake by @MGalecki10 v1.0")
window.bgcolor(BACKGROUND_COLOR)
window.setup(height=GAME_HEIGHT+300,width=GAME_WIDTH+300)
window.tracer(0)

# Score
score = 0


# Snake
snake = turtle.Turtle()
snake.speed(10)
snake.shape(SNAKE_SHAPE)
snake.color(SNAKE_COLOR)
snake.shapesize(stretch_wid=SPACE_SIZE/20, stretch_len=SPACE_SIZE/20)
snake.penup()
snake.goto(0,0)
snake.direction = "stop"
segments = []

#Border
border = turtle.Turtle()
border.speed(5)
border.pensize(4)
border.penup()
border.goto((-1/2)*(GAME_WIDTH+SPACE_SIZE),(1/2)*(GAME_HEIGHT+SPACE_SIZE))
border.pendown()
border.color('black')
border.forward(GAME_WIDTH+SPACE_SIZE)
border.right(90)
border.forward(GAME_HEIGHT+SPACE_SIZE)
border.right(90)
border.forward(GAME_WIDTH+SPACE_SIZE)
border.right(90)
border.forward(GAME_HEIGHT+SPACE_SIZE)
border.penup()
border.hideturtle()



# Food   
food = turtle.Turtle()
food_x= random.randint((-1/2)*(GAME_WIDTH/SPACE_SIZE), (1/2)*(GAME_WIDTH/SPACE_SIZE))*SPACE_SIZE
food_y= random.randint((-1/2)*(GAME_HEIGHT/SPACE_SIZE), (1/2)*(GAME_HEIGHT/SPACE_SIZE))*SPACE_SIZE
food.speed(0)
food.shape(FOOD_SIZE)
food.color(FOOD_COLOR)

food.shapesize(stretch_wid=SPACE_SIZE/20, stretch_len=SPACE_SIZE/20)
food.penup()
food.goto(food_x,food_y)

#Scoring
scoring = turtle.Turtle()
scoring.speed(5)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,((1/2)*GAME_HEIGHT) + ((1/10)*GAME_HEIGHT))
scoring.write("Score:",align="center",font=("Courier",24,"bold"))



#Function
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"
    

def go_left():
    if snake.direction != "right":
        snake.direction = "left"
    

def go_right():
    if snake.direction != "left":
        snake.direction = "right"



def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + SPACE_SIZE)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - SPACE_SIZE)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + SPACE_SIZE)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - SPACE_SIZE)

def game_over():
    time.sleep(2.5)
    window.clear()
    window.bgcolor("#c2f7f7")
    scoring.goto(0,0)
    scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
    

def borders_and_final_score():
    if snake.ycor() > (1/2)*(GAME_HEIGHT) or snake.ycor() < (-1/2)*(GAME_HEIGHT) or snake.xcor() > (1/2)*(GAME_WIDTH) or snake.xcor() < (-1/2)*(GAME_WIDTH):
        game_over()



#Controls
window.listen()
window.onkeypress(go_up,"Up")
window.onkeypress(go_down,"Down")
window.onkeypress(go_right,"Right")
window.onkeypress(go_left,"Left")



#Main game loop
while True:
    window.update()
    

    if snake.distance(food) < SPACE_SIZE:
        food_x= random.randint((-1/2)*(GAME_WIDTH/SPACE_SIZE), (1/2)*(GAME_WIDTH/SPACE_SIZE))*SPACE_SIZE
        food_y= random.randint((-1/2)*(GAME_HEIGHT/SPACE_SIZE), (1/2)*(GAME_HEIGHT/SPACE_SIZE))*SPACE_SIZE
        food.goto(food_x,food_y)
        scoring.clear()
        score+=1
        scoring.write("Score:{}".format(score),align="center",font=("Courier",24,"bold"))
        delay-=0.001
    
            

    # Create new segment of snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.shapesize(stretch_wid=SPACE_SIZE/20, stretch_len=SPACE_SIZE/20)
        new_segment.color(BODY_COLOR)
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        if snake.xcor() == segments[index].xcor() and snake.ycor() == segments[index].ycor():
            game_over()

    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)

    move()
    borders_and_final_score()
    
    time.sleep(delay)




