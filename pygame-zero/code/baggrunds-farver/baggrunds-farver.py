"""
Vil skifte bagrundes farve når musen flyttes rundt.
"""

import pygame as pg
import random

WIDTH = 500
HEIGHT = 300

def main(): 
    running = True
	
    pg.init()
    screen = pg.display.set_mode((WIDTH,HEIGHT))

    screen_rect = screen.get_rect()
    clock = pg.time.Clock()

    timer = 1000
	
    bg = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	
    while running:
        screen.fill(bg)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        curr_ticks = pg.time.get_ticks()
        if curr_ticks > timer:
            timer = curr_ticks + 1000            
            bg = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            pg.display.update()
            
        
        clock.tick(1000)                  
        		

if __name__ == '__main__':
    main()