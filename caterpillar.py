import turtle as t
import random as rd

t.bgcolor('yellow')

caterpillar = t.Turtle()  # initializing the turtles
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()       # move your pen up from the page ie dont draw
caterpillar.hideturtle()   # hide it for now dont display it yet

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14)) # a hexagon shaped leaf
t.register_shape('leaf',leaf_shape) # a method to register a shape using the points allocated
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

game_started = False  # setting a variable as False so that maybe used below with while loop
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start',align='center',font=('Arial',16,'bold')) #method to write in turtles
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outside_window():  # declaring a working window for caterpillar
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = caterpillar.pos()  # a method to get the coordinates of cursor into variables
    outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
    return outside

def game_over(): # all things will get background color
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center' , font=('Aerial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    # defining the 1st quadrant below
    x = (t.window_width() / 2)-50
    y = (t.window_height() / 2)-50
    score_turtle.setpos(x,y) # a method to allocate the position of a turtle
    # entering your current score that is passed into the function
    score_turtle.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))

def place_leaf():
    # firstly always hide the turtle when function is called and then
    # place it randomly
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def start_game():
    global game_started
    # now when game has already started and someone presses the spacebar again
    # then it should return nothing
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear() # clear up that PRESS ANY KEY TO START shit

    caterpillar_speed = 2   # initial speed ,
    caterpillar_length = 3  # initial length
    caterpillar.shapesize(1,caterpillar_length,1)    #will have 3 boxes
    caterpillar.showturtle()      # the caterpillar that was hidden on line 10 , now display it
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf)<20:
            place_leaf()
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)    # functioned is called with given score of 0
        if outside_window():  # when that condition is true
            game_over()
            break
# now defining the keys
# 0 is for left , 180 for right , 90 for up and 270 for down
def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180: # heading method states the direction ie by angle
        caterpillar.setheading(90)  # setheading sets the direction to particular angle

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

# onkey method fires a function , when a certain key is pressed
t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()  # this method kind of stores the onkey attributes and requiers the program to listen to them
t.mainloop() # a method that executes the main loop
