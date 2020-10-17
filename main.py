from game import Game
from gameDraw import GameDraw
from mySocket import MySocket
import pygame, sys

#region game init
gameDraw = GameDraw()
game = Game()
sock=MySocket()

type=""
sel=input("S or C\n")
if(sel in ["s","S"]):
    type="s"
    sock.server()
    sock.serverConnect()

elif(sel in ["c","C"]):
    type="c"
    sock.clientConnect(1234)
#endregion

#region gameloop
running=True
gameDraw.updateScreen(game)
pygame.display.flip()
while running:
    for event in pygame.event.get():
        print(pygame.event.get())
        if event.type==pygame.QUIT:
            running=False

        if(game.running):
            if(type=="s"):
                if(game.turn=="player1"): #turno do player 1
                    if event.type == pygame.KEYDOWN:
                        print(event.key)
                        game.moveplayer1(event.key)
                        gameDraw.updateScreen(game)
                        pygame.display.flip()

                        sock.sendGame(game)

                elif(game.turn=="player2"):
                    game=sock.receiveGame()
                    gameDraw.updateScreen(game)
                    pygame.display.flip()
                    
                    pygame.event.clear()

            if(type=="c"):
                if(game.turn=="player2"): #turno do player 2
                    if event.type == pygame.KEYDOWN:
                        print(event.key)
                        game.moveplayer2(event.key)
                        gameDraw.updateScreen(game)
                        pygame.display.flip()

                        sock.sendGame(game)
                
                elif(game.turn=="player1"):
                    game=sock.receiveGame()
                    gameDraw.updateScreen(game)
                    pygame.display.flip()

                    pygame.event.clear()



            # game.checkPlayerOverTail()
        else:
            print(f"{game.winner} winned the game!\n press ANY KEY in game to close")
            if (event.type == pygame.KEYDOWN):
                running=False

pygame.quit()
#endregion

