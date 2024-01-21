# ping-pong
import turtle 

# setup window ==================
window= turtle.Screen()
window.title("Ping Pong Game")
window.setup(width=800,height=600)
window.tracer(0) #set delay for update drawing
window.bgcolor(.1 , .1, .1 )

#setup game object ===================
#ball

ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")

#scale factor * default size ()
ball.shapesize(stretch_len=1 , stretch_wid=1 )
ball.goto(x=0,y=0)
ball.penup() # stop drawing lines when moving
ball_dx=1
ball_dy=1
ball_speed= 0.3
#center line
center_line=turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.color("white")
# width => 500px = 25 * 20px default
center_line.shapesize(stretch_len=.1, stretch_wid=25)
center_line.penup()
center_line.goto(0,0)
# player1
player1= turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.shapesize(stretch_len=1,stretch_wid=5 )
player1.color("blue")
player1.penup()
player1.goto(-350, 0 )

# player2
player2= turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.shapesize(stretch_len=1,stretch_wid=5 )
player2.color("red")
player2.penup()
player2.goto(350, 0 )

#score

score= turtle.Turtle()
score.speed(0)
score.color("white")
score.penup
score.goto(0 , 260)
score.write("Player 1: 0 Player 2: 0 ",align="center",font=("courier",14, "normal"))     
score.hideturtle()
p1_score, p2_score =0 , 0 # variables to hold player 1 and 2
# Players movement =============================

players_speed=25
def p1_move_up():
    player1.sety(player1.ycor()+ players_speed)

def p1_move_down():
    player1.sety(player1.ycor()- players_speed)


def p2_move_up():
    player2.sety(player2.ycor()+ players_speed)


def p2_move_down():
    player2.sety(player2.ycor()- players_speed)


#
window.listen()
window.onkeypress(p1_move_up, "z")
window.onkeypress(p1_move_down, "s")
window.onkeypress(p2_move_up, "Up")
window.onkeypress(p2_move_down, "Down")



#Game loop =========================
while True:
    window.update()

    # ball movement
    ball.setx(ball.xcor()+ (ball_dx * ball_speed) )
    ball.sety(ball.ycor()+ (ball_dy * ball_speed) )

    if(ball.ycor()> 290 ):
        ball.sety(290)
        ball_dy *= -1 # invert Y direction

    if(ball.ycor() < -290 ):
        ball.sety(-290)
        ball_dy *= -1 # invert Y direction

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (player1.ycor()-60) and ball.ycor() < (player1.ycor()+60) :
        ball.setx(-340)
        ball_dx *= -1

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (player2.ycor()-60) and ball.ycor() < (player2.ycor()+60) :
        ball.setx(340)
        ball_dx *= -1

    if(ball.xcor() > 390):
        ball.goto(0, 0)
        ball_dx *= -1 # invert X direction
        score.clear()
        p1_score +=1
        score.write(f"Player 1: {p1_score} Player 2: {p2_score} ",align="center",font=("courier",14, "normal"))     


    if(ball.xcor() < -390):
        ball.goto(0, 0)
        ball_dx *= -1 # invert X direction
        score.clear()
        p2_score +=1
        score.write(f"Player 1: {p1_score} Player 2 : {p2_score}",align="center",font=("courier",14, "normal"))
