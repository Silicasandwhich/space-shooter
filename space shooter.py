import random
import pyxel
import math

pyxel.init(255, 255)

playerX = 125
playerY = 200
spawnCounter = 0
moveCounter = 0
score = 0
speedScore = 0
lives = 3

shots = []
enemies = [[128, 50]]


def shoot():
    shots.append([playerX, playerY-15])


def spawn_enemy():
    enemies.append([random.randint(0, 255), random.randint(0, 100)])


def update():
    # globals
    global speedScore
    global playerX
    global shots
    global spawnCounter
    global moveCounter
    global enemies
    global score
    global lives
    # player input
    if pyxel.btn(pyxel.KEY_D):
        playerX += 3
    if pyxel.btn(pyxel.KEY_A):
        playerX -= 3
    if pyxel.btnp(pyxel.KEY_SPACE):
        shoot()
    # screen boundaries
    if playerX >= 255:
        playerX = 255
    elif playerX <= 0:
        playerX = 0
    # moving shots
    for x in shots:
        x[1] -= 5
    # spawn enemies
    spawnCounter += speedScore / 500 + 1
    if spawnCounter >= 100:
        spawnCounter = 0
        spawn_enemy()
    # move enemies
    moveCounter += speedScore / 500 + 1
    if moveCounter >= 50:
        moveCounter = 0
        for enemy in enemies:
            enemy[0] += random.randint(-30, 30)
            enemy[1] += 10
            if enemy[0] >= 255:
                enemy[0] = 255
            if enemy[0] <= 0:
                enemy[0] = 0
    # collision detection
    for enemy in enemies:
        for shot in shots:
            if enemy[0] + 4 >= shot[0] >= enemy[0] - 4:
                if enemy[1] + 4 >= shot[1] >= enemy[1] - 4:
                    shots.remove(shot)
                    enemies.remove(enemy)
                    score += 50
                    speedScore += 50
    # lose a life if an enemy passes the player
    for enemy in enemies:
        if enemy[1] >= 200:
            enemies.remove(enemy)
            lives -= 1
            if lives < 0:
                lives = 0
            speedScore -= 500
            if speedScore < 0:
                speedScore = 0


def draw():
    pyxel.cls(0)
    # player
    pyxel.circ(playerX, playerY, 5, 3)
    # shots
    for x in shots:
        pyxel.line(x[0], x[1], x[0], x[1] + 7, 2)
    # enemies
    for enemy in enemies:
        pyxel.circ(enemy[0], enemy[1], 3, 7)
    # score
    pyxel.text(15, 230, "Score: " + str(score), 7)

    # lives
    pyxel.text(210, 230, "Lives: " + str(lives), 7)

    # speed
    pyxel.text(210, 25, "Speed: " + str(round(speedScore / 500 + 1, 2)) + 'x', 7)


pyxel.run(update, draw)
