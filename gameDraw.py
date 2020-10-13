import pygame, sys

class GameDraw:
    def __init__(self,screen):
        self.screen = screen
    
    def drawPlayer(self,pos, color):
        posX=pos["x"]*(500/10)
        posY=pos["y"]*(500/10)
        pygame.draw.rect(self.screen,color,[posX,posY,50,50])
    
    def drawTail(self,tail, color):
        for pos in tail:
            posX=pos["x"]*(500/10)
            posY=pos["y"]*(500/10)
            pygame.draw.rect(self.screen,color,[posX,posY,50,50])

    def updateScreen(self,game):
        #player1
        self.drawTail(game.player1Tail,[219, 116, 116])
        self.drawPlayer(game.player1,[219,72,72])

        #player2
        self.drawTail(game.player2Tail,[114, 114, 219])
        self.drawPlayer(game.player2, [72,72,219])
