#A Game of Snake using Python - www.101computing.net/snake-game-using-python/
import turtle
import turtle
import time
from snake import Snake
from apple import Apple

def displayInstructions():
   print("~~~~~~~~~~~~~~~~~~~~")
   print("~                  ~")
   print("~   Snake Game     ~")
   print("~                  ~")
   print("~~~~~~~~~~~~~~~~~~~~")
   print("")
   print("~~~ Instructions ~~~")
   print(" > Use the arrow keys on your keyboard to control the snake.")
   print(" > Do not let your snake reach the edges of the screen.")
   print(" > Direct your snake to reach the red apple.")
   print(" > Do not let your snake eat/cross its own tail.")
   print("~~~~~~~~~~~~~~~~~~~~")
   print("")
   print(" >>> Double click on the screen to get started...")
   print("")

def drawBorders():
   pen = turtle.Turtle()
   pen.hideturtle()  
   pen.speed(5)
   pen.color("#FFFFFF")
   pen.pensize(2)
   pen.penup()
   pen.goto(-199,-199)
   pen.pendown()
   for i in range(4):
      pen.forward(398)
      pen.left(90)

# >>> Setup the Stage
screen = turtle.Screen()
screen.tracer(0,0)
screen.setup(400, 400)
screen.bgcolor((200,200,200))

# >>> Draw the white borders
drawBorders()
  
# >>> Add the apple
apple = Apple("#FF0000",random.randint(0,19),random.randint(0,19))
apple.draw()

# >>> Add the Snake...
snake = Snake("#810081","#B130B1",0,19)  #Purple Snake in the bottom left corner (0,0) of the 20x20 grid
snake.direction = "right"
snake.draw()

# >>> Display instructions on how to play the game
displayInstructions()

def startGame(x,y):
   global gameOver
   if not gameOver:
      score = 0
      delay = 0.25
      print(" >>> Starting Game")
    
      # >>> Main game loop
      while not gameOver:  
         screen.bgcolor((200,200,200))
         snake.move() 
  
         # Has the snake gone over the edge of the game window?
         if snake.isOffScreen():
            print(" >>> Game Over! <<<")
            gameOver=True
        
         #Is the snake biting its own tail!  
         elif snake.isBitingTail():
            print(" >>> Game Over! <<<")
            gameOver=True
        
         # Has the snake reached the apple? 
         elif snake.position[0] == apple.position[0] and snake.position[1] == apple.position[1]:
            snake.score += 1
            print("Score: " + str(snake.score) + "pts")
            # Extend the tail of the snake
            snake.grow()
            # Respawn the apple using a different location
            apple.respawn()
   
         screen.update()
         time.sleep(delay)


# >>> Implementing motion of the snake in all 4 directions
def go_up():
   snake.direction = "up"

def go_down():
   snake.direction = "down"
  
def go_right():
   snake.direction = "right"
 
def go_left():
   snake.direction = "left"

# >>> Keyboard bindings (using the arrow keys)
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")

#The game will only start once the player clicks on the screen
screen.onscreenclick(startGame, 1)

gameOver=False
screen.mainloop()