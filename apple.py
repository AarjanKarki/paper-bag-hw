import pgzrun, random
WIDTH=500
HEIGHT=500
paper=Actor('paper')
paper.pos=250,470
score=0
dinosaur=Actor('jump5')
dinosaur.x=random.randint(20,480)
dinosaur.y=0
gameover=False

def draw():
    screen.clear()
    screen.fill('white')
    paper.draw()
    dinosaur.draw()
    screen.draw.text('Score:'+str(score),color='black',topleft=(10,10))
    if gameover==True:
      screen.fill('red')
      screen.draw.text('Game over! Your final score:'+str(score),midtop=(WIDTH/2,10),
      fontsize=40, color='black')

def place_dinosaur():
   dinosaur.x=random.randint(20,480)
   dinosaur.y=0

def time_up():
    global gameover
    gameover=True


def update():
    global score  
    dinosaur.y+=2+score/10
    if dinosaur.y>HEIGHT:
        place_dinosaur()
    if keyboard.left:
        paper.x-=5+score/10
    if keyboard.right:
        paper.x+=5+score/10
    if paper.colliderect(dinosaur):
        score=score+10
        place_dinosaur()
    

clock.schedule(time_up,20.0)


    
    
    




pgzrun.go()
