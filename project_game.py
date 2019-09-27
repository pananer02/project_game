#Example 10-2
import pgzrun
from random import randint


#function for display
def draw():
    screen.blit('backdrop800',(0,0))
    ship.draw()
    alien.draw()
    Minialien.draw()
    for bullet in bullets:
        bullet.draw()
    screen.draw.text("score :"+str(score),
    topleft=(10,10),fontsize=28,color='white')

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor('bullet'))
        last = len(bullets)
        bullets[last-1].pos = ship.pos

def update():
    global statusBoss,EnemyMiniBoss,statusMini,score,Time
    #check key
    if keyboard.LEFT:
        ship.x -= 3
        if ship.left < 0:
            ship.left = 0
    elif keyboard.RIGHT:
        ship.x +=3
        if ship.right > WIDTH:
            ship.right = WIDTH
    #move bullets
    for bullet in bullets:
        bullet.y -= 5
        if bullet.top <0:
            bullets.remove(bullet)
    #move alien
    if statusBoss == 0:
        alien.left += 2
        if alien.left > WIDTH-200 :
            alien.left = WIDTH-200
            statusBoss = 1
    elif statusBoss == 1:
        alien.left -= 2
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
   
    #collision alien
    for bullet in bullets:
        if bullet.y < 100:
            if bullet.colliderect(alien):
                Minialien.pos = (randint(0,WIDTH),125)
                alien.pos = (4000,1250)
                bullets.remove(bullet) 
                statusBoss = 2
                statusMini = 0
                EnemyMiniBoss += 1
                score += 1
            if bullet.colliderect(Minialien):
                if(EnemyMiniBoss % 10 == 0):
                    alien.pos = (randint(0,WIDTH),125)
                    Minialien.pos = (4000,1250)
                    bullets.remove(bullet)
                    EnemyMiniBoss += 1
                    statusMini = 2
                    statusBoss = 0
                    score += 1
                else:
                    Minialien.pos = (randint(0,WIDTH),125)
                    bullets.remove(bullet)
                    EnemyMiniBoss += 1
                    score += 1


def time_count():
    global Time
    Time -= 1

def time_out():
    global StatusGame
    StatusGame = 2
    clock.unschedule(time_count)

#main
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
alien.pos = (400,125)
Minialien = Actor('small')
Minialien.pos = (10000,10000)
bullets = []
clock.schedule_interval(time_count,1)
clock.schedule(time_out,MaxTime)
pgzrun.go()

        
