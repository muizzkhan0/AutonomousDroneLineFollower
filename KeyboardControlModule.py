import pygame
import time

def init():
    pygame.init()
    window = pygame.display.set_mode((400,400))

def getKey(keyName):
    ans = False
    for event in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey("w"):
        print("W")
    if getKey("a"):
        print("A")
    if getKey("s"):
        print("S")
    if getKey("d"):
        print("D")
    time.sleep(0.25)

if __name__ == '__main__':
    init()
    while True:
        main()