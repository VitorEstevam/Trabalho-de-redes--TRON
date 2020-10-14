from game import Game
from gameDraw import GameDraw
import pygame, sys

#region game init
gameDraw = GameDraw()
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

        if(game.running):
            if(game.turn=="player1"): #turno do player 1
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    game.moveplayer1(event.key)
                    gameDraw.updateScreen(game)
                    pygame.display.flip()
            
            elif(game.turn=="player2"):
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    game.moveplayer2(event.key)
                    gameDraw.updateScreen(game)
                    pygame.display.flip()

            game.checkPlayerOverTail()
        else:
            print(f"{game.winner} winned the game!\n press ANY KEY in game to close")
            if (event.type == pygame.KEYDOWN):
                running=False

pygame.quit()
#endregion

