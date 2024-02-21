# Write your code here :-)
import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_blue')
ship.x = 400
ship.y = 400

def draw():
    ship.draw()

pgzrun.go()
