import pyxel
import random

pyxel.init(255, 255)

playerX = 125
playerY = 200
spawnCounter = 0
moveCounter = 0
score = 0
lives = 3

shots = []
enemies = [[128, 50]]


def shoot():
    shots.append([playerX, playerY-15])


def spawn_enemy():
    enemies.append([random.randint(0, 255), random.randint(0, 100)])


def update():
    # globals
    global playerX
    global shots
    global spawnCounter
    global moveCounter
    global enemies
    global score
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
    spawnCounter += 1
    if spawnCounter % 100 == 0:
        spawn_enemy()
    # move enemies
    moveCounter += 1
    if moveCounter % 50 == 0:
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
            if enemy[0] + 3 >= shot[0] >= enemy[0] - 3:
                if enemy[1] + 3 >= shot[1] >= enemy[1] - 3:
                    shots.remove(shot)
                    enemies.remove(enemy)
                    score += 50


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


pyxel.run(update, draw)
