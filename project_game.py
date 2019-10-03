#Example 10-2
import pgzrun
from random import randint


#function for display
def draw():
    screen.fill((100,200,200))
    if StatusGame == 0:
        message = "Are you ready, press Enter key to play."
        screen.draw.text(message,topleft=(20,350),fontsize=40,color='blue')
    elif StatusGame == 1:
        screen.blit('backdrop800',(0,0))
        ship.draw()
        alien.draw()
        Minialien.draw()
        for bullet in bullets:
            bullet.draw()
        for fruit in fruits:
            fruit.draw()
        screen.draw.text("Score : "+str(score),topleft=(10,10),fontsize=30,color='white')  
        screen.draw.text("<- don't touch",topleft=(90,50),fontsize=30,color='white')
        screen.draw.text("Time : "+str(Time),topleft=(500,10),fontsize=30,color='white')
        screen.draw.text("Bullet :"+str(len(bullets)),topleft=(10,600),fontsize=28,color='white')
    elif StatusGame == 2:
        screen.fill((200,100,200))
        message = "Game over, your score : " + str(score)
        screen.draw.text(message,topleft=(20,270),fontsize=50,color='cyan')
        message = "Play again,press Enter key ."
        screen.draw.text(message,topleft=(20,350),fontsize=50,color='cyan')
        
def on_key_down(key):
    global StatusGame,Score,Time
    if StatusGame == 0:
        if key == keys.RETURN:
            start_game()
    elif StatusGame == 2 :
        if key == keys.RETURN:
            start_game()
    if key == keys.SPACE:
        bullets.append(Actor('bullet'))
        last = len(bullets)
        bullets[last-1].pos = ship.pos
        sounds.pop.play()

def update():
    global statusBoss,EnemyMiniBoss,statusMini,score,Time,StatusGame,MaxFruits,bossCount,fruits,speed
    #check key
    if keyboard.LEFT:
        ship.x -= 5
        if ship.left < 0:
            ship.left = 0
    elif keyboard.RIGHT:
        ship.x += 5
        if ship.right > WIDTH:
            ship.right = WIDTH
    elif keyboard.up:
        ship.y -= 5
        if ship.y < 450:
            ship.y = 450
    elif keyboard.down:
        ship.y += 5
        if ship.y > HEIGHT:
            ship.y = HEIGHT
    #move bullets
    for bullet in bullets[:]:
        bullet.y -= 5
        if bullet.top <-100:
            bullets.remove(bullet)
    #move alien
    if statusBoss == 0:
        alien.left += 5
        if alien.left > WIDTH-200 :
            alien.left = WIDTH-200
            statusBoss = 1
    elif statusBoss == 1:
        alien.left -= 5
        if alien.right < 200:
            alien.right = 200
            statusBoss = 0
    else :
        alien.left += 0
    if statusMini == 0:
        Minialien.left += 4
        if Minialien.left > WIDTH-100:
            Minialien.left = WIDTH-100
            statusMini = 1
    elif statusMini == 1:
         Minialien.left -= 4
         if Minialien.right < 100:
            Minialien.right = 100
            statusMini = 0
    else :
        Minialien.left += 0

    #Enemy shoot
    global StatusGame,MaxFruits
    if StatusGame == 1:
        for n in range(MaxFruits):
            fruits[n].top += speeds[n]
            if(fruits[n].top > HEIGHT+100):
                fruits[n].bottom = -100
    #collision alien
    for bullet in bullets:
        if bullet.colliderect(alien):
            print("hitboss")
            bullets.remove(bullet)
            if(bossCount % 2 ==0):
                Minialien.pos = (-100,125)
                alien.pos = (4000,1250)   
                statusBoss = 2
                statusMini = 0
                EnemyMiniBoss += 1
                score += 5
                bossCount += 1
            elif(bossCount % 2 ==1):
                Minialien.pos = (1000,125)
                alien.pos = (4000,1250)   
                statusBoss = 2
                statusMini = 0
                EnemyMiniBoss += 1
                score += 5
                bossCount += 1   
        elif bullet.colliderect(Minialien):
            print("hit")
            bullets.remove(bullet)
            if(EnemyMiniBoss % 10 == 0):
                Minialien.pos = (4000,1250)
                if(bossCount % 2 == 0):
                    alien.pos = (-100,125)
                    EnemyMiniBoss += 1
                    statusMini = 2
                    statusBoss = 0
                    score += 1
                elif(bossCount % 2 == 1):
                    alien.pos = (1000,125)
                    EnemyMiniBoss += 1
                    statusMini = 2
                    statusBoss = 0
                    score += 1
            else:
                if(score % 2 == 0):
                    Minialien.pos = (-100,125)
                    EnemyMiniBoss += 1 
                    score += 1
                elif(score % 2 == 1):
                    Minialien.pos = (1000,125)
                    EnemyMiniBoss += 1
                    score += 1
        if StatusGame == 1:
            for fruit in fruits:
                if fruit.y < HEIGHT-100:
                     if fruit.colliderect(ship):
                        score -= 10
                        fruits.remove(fruit)
                        a = randint(0,2)
                        fruits.append(Actor('apple'))
                        speeds.append(randint(1,4))
                        fruits[2].pos = POS[a]
    
def start_game():
    global StatusGame,Time,score,MaxFruits,fruits,speed

    StatusGame = 1
    Time = 60
    score = 0
    MaxFruits = 3
    Minialien.pos = (400,125)
    alien.pos = (4000,1250)
    for n in range(MaxFruits) :
        fruits.append(Actor('apple'))
        speeds.append(randint(2,4))
        fruits[n].pos = (0,0)
    for n in range(MaxFruits) :
        fruits.append(Actor('apple'))
        speeds.append(randint(2,4))
        fruits[n].pos = POS[n]  
    clock.schedule_interval(time_count,1)
    clock.schedule(time_out,MaxTime)

def time_count():
    global Time
    Time -= 1
    

def time_out():
    global StatusGame
    StatusGame = 2
    Minialien.pos = (4000,1250)
    alien.pos = (4000,1250)
    clock.unschedule(time_count)
    
#main
POS = [(150,0),(320,0),(560,0)]
bossCount = 0
MaxFruits = 3
StatusGame = 0
Time = 60
score = 0
EnemyMiniBoss = 1
statusMini = 0
statusBoss = 0
hit = 0
MaxTime = 60
WIDTH = 600
HEIGHT = 700
ship = Actor('me')
ship.pos = (WIDTH/2,HEIGHT-40)
alien = Actor('enemy')
alien.pos = (400,175)
Minialien = Actor('small')
Minialien.pos = (10000,10000)
fruits = []
speeds = []
bullets = []
pgzrun.go()

        
