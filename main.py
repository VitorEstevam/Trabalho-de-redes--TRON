from game import Game
from gameDraw import GameDraw
import pygame, sys

#region screen init
screen=pygame.display.set_mode([500, 500])
screen.fill([255, 255, 255])

gameDraw = GameDraw(screen)
#endregion

#region game init
game = Game()
#endregion


#region gameloop
running=True
gameDraw.updateScreen(game)
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            print("APERTOU")
            print(event.key)
            game.moveplayer1(event.key)
            gameDraw.updateScreen(game)
            pygame.display.flip()

pygame.quit()
#endregion


