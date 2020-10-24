import pygame, sys

from game import Game
from gameDraw import GameDraw
from mySocket import MySocket
from window import Window


#region game init
gameDraw = GameDraw()
game = Game()
sock=MySocket()
window = Window()

type=""
sel=window.playerType()
if(sel in ["s","S"]):
    type="s"
    sock.server()
    window.showPort(sock.port)
    sock.serverConnect()
    window.showColor("VERMELHO")

elif(sel in ["c","C"]):
    type="c"

    endereco,porta = window.askPort()
    if(endereco==""):
        sock.clientConnect(1234)
    else:
        sock.clientConnect(1234,endereco)

    window.showColor("AZUL")
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
                        game.checkPlayerOverTail()
                        #send game
                        sock.sendGame(game)

                elif(game.turn=="player2"):
                    game=sock.receiveGame()
                    gameDraw.updateScreen(game)
                    pygame.display.flip()
                    #clean event list
                    pygame.event.clear()
                    #update game win-defeat state
                    game.checkPlayerOverTail()

            if(type=="c"):
                if(game.turn=="player2"): #turno do player 2
                    if event.type == pygame.KEYDOWN:
                        print(event.key)
                        game.moveplayer2(event.key)
                        gameDraw.updateScreen(game)
                        pygame.display.flip()
                        #update game win-defeat state
                        game.checkPlayerOverTail()
                        #send game
                        sock.sendGame(game)
                
                elif(game.turn=="player1"):
                    game=sock.receiveGame()
                    #update visuals
                    gameDraw.updateScreen(game)
                    pygame.display.flip()
                    #clean event list
                    pygame.event.clear()
                    #update game win-defeat state
                    game.checkPlayerOverTail()
    
        else:
            running=window.endGame(game.winner)

pygame.quit()
#endregion

