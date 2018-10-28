import pyxel

pyxel.init(255, 255)

playerX = 125
playerY = 200
spawnCounter = 0
shots = []


def shoot():
    shots.append([playerX, playerY-15])


def update():
    # globals
    global playerX
    global shots
    global spawnCounter
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


def draw():
    pyxel.cls(0)
    # player
    pyxel.circ(playerX, playerY, 5, 3)
    # shots
    for x in shots:
        pyxel.line(x[0], x[1], x[0], x[1] + 7, 2)


pyxel.run(update, draw)
