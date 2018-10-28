import random
import pyxel

pyxel.init(255, 255)

startWave = [[128, 50], [50, 50], [32, 50], [64, 60]]
playerX = 125
playerY = 200
spawnCounter = 0
moveCounter = 0
score = 0
speedScore = 0
lives = 3
sessionHighSpeed = 1
highScore = 0
highSpeed = 1
screen = "Start"
textColor = 1
textCounter = 0

shots = []
enemies = startWave


def shoot():
    shots.append([playerX, playerY-15])


def spawn_enemy():
    enemies.append([random.randint(0, 255), random.randint(0, 100)])


def update():
    # globals
    global playerY
    global highScore
    global highSpeed
    global speedScore
    global playerX
    global shots
    global spawnCounter
    global moveCounter
    global enemies
    global score
    global lives
    global sessionHighSpeed
    global screen
    global textColor
    global textCounter
    if screen == "Game":
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
                    enemy[0] = 230
                if enemy[0] <= 0:
                    enemy[0] = 30
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
                    if score > highScore:
                        highScore = score
                    if sessionHighSpeed > highSpeed:
                        highSpeed = sessionHighSpeed
                    screen = "Game Over"
                speedScore -= 500
                if speedScore < 0:
                    speedScore = 0
        # change session high speed
        if sessionHighSpeed < speedScore / 500 + 1:
            sessionHighSpeed = speedScore
    elif screen == "Game Over":
        if pyxel.btnp(pyxel.KEY_Z):
            screen = "Start"
    elif screen == "Start":
        textCounter += 1
        if textCounter % 30 == 0:
            textColor = random.randint(1, 12)
        if pyxel.btnp(pyxel.KEY_SPACE):
            playerX = 125
            playerY = 200
            spawnCounter = 0
            moveCounter = 0
            score = 0
            speedScore = 0
            lives = 3
            sessionHighSpeed = 1
            shots = []
            enemies = startWave
            screen = "Game"


def draw():
    if screen == "Game":
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
    if screen == "Game Over":
        pyxel.cls(0)
        pyxel.text(120, 55, "Game Over", 7)
        pyxel.text(75, 78, "Score: " + str(score), 7)
        pyxel.text(175, 78, "High: " + str(highScore), 7)
        pyxel.text(75, 140, "Speed: " + str(sessionHighSpeed) + 'x', 7)
        pyxel.text(175, 140, "High: " + str(highSpeed) + 'x', 7)
        pyxel.text(120, 200, "Press 'Z' to continue")
    if screen == "Start":
        pyxel.cls(0)
        pyxel.text(107, 100, "SPACE SHOOTER", textColor)
        pyxel.text(105, 175, "Space To Start", round(textColor+15/2))


pyxel.run(update, draw)
