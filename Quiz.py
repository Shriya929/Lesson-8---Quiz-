import pgzrun
WIDTH = 600
HEIGHT = 400
introduction = Rect(4,0,590,50) 
question = Rect(5,70,402,100)
answer_1 = Rect(5,180,200,100)
answer_2 = Rect(210,180,200,100)
answer_3 = Rect(5,290,200,100)
answer_4 = Rect(210,290,200,100)
timer = Rect(420,70,110,100)

count_down = 10
def draw():
    screen.fill("black")
    screen.draw.filled_rect(introduction,"black")
    screen.draw.textbox("Welcome to Quiz Master!",introduction,color = "White")
    screen.draw.filled_rect(question,"blue")
    screen.draw.filled_rect(answer_1,"orange")
    screen.draw.filled_rect(answer_2,"red")
    screen.draw.filled_rect(answer_3,"green")
    screen.draw.filled_rect(answer_4,"grey")
    screen.draw.filled_rect(timer,"yellow")
    screen.draw.textbox(str(count_down),timer,color = "black")
def update():
    introduction.x = introduction.x - 4
    if introduction.right <=0:
        introduction.left = 600
def count_down_update():
    global count_down
    if count_down > 0:
        count_down = count_down - 1    
clock.schedule_interval(count_down_update, 1)
pgzrun.go()