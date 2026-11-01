import pgzrun
WIDTH = 600
HEIGHT = 400
introduction = Rect(4,0,590,50) 
question = Rect(5,80,400,100)
def draw():
    screen.fill("black")
    screen.draw.filled_rect(introduction,"red")
    screen.draw.textbox("Welcome to Quiz Master!",introduction,color = "White")
    screen.draw.filled_rect(question,"blue")
pgzrun.go()