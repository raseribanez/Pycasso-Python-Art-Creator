#!usr/bin/env/python
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
screencaption=pygame.display.set_caption('Pycasso Image Creator - Ben Woodfield')
screen=pygame.display.set_mode([640,640])
screen.fill([0,0,0])# black background

def random_color():
    rgbl = [255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

# Hash or unHash the circles or rectangles below
for i in range(30):
    radius=random.randint(0,100)
    width=random.randint(0,255)
    height=random.randint(0,100)
    top=random.randint(0,400)
    left=random.randint(0,500)
    pygame.draw.circle(screen, random_color(),[top,left],radius)#,1)  ### Circles
    pygame.draw.rect(screen, random_color(),[left,top,width,height])#,3)### Rectangles
    # Above: If you remove the comment hash and include the number, shapes will not be filled

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
