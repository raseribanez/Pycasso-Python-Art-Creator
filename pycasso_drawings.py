#usr/bin/env/python
# Ben Woodfield
# Pygame random positioning drawing
# Turn Python into an Artist!

__author__ = "Ben Woodfield"
__copyright__ = "Copyright (C) 2004 Author Name"
__license__ = "GNU Public"
__version__ = "1.0"

import pygame,sys
import random

pygame.init()
screencaption=pygame.display.set_caption('hello world')
screen=pygame.display.set_mode([640,640])
screen.fill([205,255,255])

# Hash or unHash the circles or rectangles below
for i in range(30):
    radius=random.randint(0,100)
    width=random.randint(0,255)
    height=random.randint(0,100)
    top=random.randint(0,400)
    left=random.randint(0,500)
    pygame.draw.circle(screen,[0,0,255],[top,left],radius,1)  ### Circles
    pygame.draw.rect(screen,[0,0,255],[left,top,width,height],3)### Rectangles

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
