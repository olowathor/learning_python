import pygame
import random
from blob import Blob
import numpy as np
import logging

logging.basicConfig(filename='logfile.log',level=logging.INFO) #DEBUG, WARNING, ERROR, CRITICAL

'''
DEBUG	Detailed information, typically of interest only when diagnosing problems.
INFO	Confirmation that things are working as expected.
WARNING	An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR	Due to a more serious problem, the software has not been able to perform some function.
CRITICAL	A serious error, indicating that the program itself may be unable to continue running.
'''

STARTING_BLUE_BLOBS = 40
STARTING_RED_BLOBS = 30
STARTING_GREEN_BLOBS = int(STARTING_BLUE_BLOBS/5)

WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob World!") 
clock = pygame.time.Clock()


class RedBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (255,0,0) , x_boundary, y_boundary)

    def move_fast(self):
        self.x += random.randrange(-4,5)
        self.y += random.randrange(-4,5)

    def __add__(self, other_blob):
        logging.info('Blob add op {} + {}'.format(repr(self), str(other_blob)))
        if other_blob.color == (0,0,255):
            self.size -= other_blob.size
            other_blob.size -= self.size
        elif other_blob.color == (0,255,0):
            self.size += other_blob.size
            other_blob.size = 0
        elif other_blob.color == (255,0,0):
            pass
        else:
            raise Exception('Tried to combine one or multiple blobs of unsupported colors.')


class GreenBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0,255,0) , x_boundary, y_boundary)

    def move_fast(self):
        self.x += random.randrange(-6,7)
        self.y += random.randrange(-6,7)


class BlueBlob(Blob):
    '''
    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(color, x_boundary, y_boundary)
        self.color = BLUE              
    '''

    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0,0,255) , x_boundary, y_boundary)

    def move_fast(self):
        self.x += random.randrange(-5,6)
        self.y += random.randrange(-5,6)


def is_touching(b1,b2):
    return np.linalg.norm(np.array([b1.x,b1.y])-np.array([b2.x,b2.y])) < (b1.size + b2.size)

def handle_collisions(blob_list):
    reds, greens, blues  = blob_list

    for red_id, red_blob in reds.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                logging.debug('Checking if blobs are touching {} + {}'.format(repr(red_blob),str(other_blob)))
                if red_blob == other_blob:
                    pass
                else:
                    if is_touching(red_blob, other_blob):
                        red_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if red_blob.size <= 0:
                            del reds[red_id]

    return reds, greens, blues 

def draw_environment(blob_list):
    game_display.fill(WHITE)
    reds, greens, blues  = handle_collisions(blob_list)

    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x,blob.y], blob.size) 
            blob.move_fast()
            blob.check_bounds()

    pygame.display.update()

    return reds, greens, blues
     
def main():
    red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH,HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
    blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))

    '''    
    print('Blue blob size: {}, red blob size: {}'.format(blue_blobs[0].size,red_blobs[0].size))
    blue_blobs[0] + red_blobs[0]
    print('Blue blob size: {}, red blob size: {}'.format(blue_blobs[0].size,red_blobs[0].size))
    '''

    while True:
        try:        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            red_blobs, green_blobs, blue_blobs = draw_environment([red_blobs,green_blobs,blue_blobs])
            clock.tick(60)

        except Exception as e:
            logging.critical(str(e))
            pygame.quit()
            quit()
            break        
if __name__ == '__main__':
    main()
