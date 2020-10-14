import pygame, sys

class GameDraw:
    player1background=[222, 191, 191]
    player2background=[189, 189, 219]
    player1color=[219,72,72]
    player2color=[72,72,219]

    def __init__(self):
        self.screen=pygame.display.set_mode([500, 500])
        self.screen.fill([255, 255, 255])
        #self.drawGrid([219, 116, 116])
    
    def drawGrid(self,color):
        for i in range(10):
            #vertical lines
            pygame.draw.line(self.screen,color,[(500/10)*i,0],[(500/10)*i,500])
            #horizontal lines
            pygame.draw.line(self.screen,color,[0,(500/10)*i],[500,(500/10)*i])

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
        #fill background
        self.screen.fill(self.player1background if game.turn=="player1" else self.player2background )

        #tails
        self.drawTail(game.player1Tail,[219, 116, 116])
        self.drawTail(game.player2Tail,[114, 114, 219])

        #players
        self.drawPlayer(game.player1, self.player1color)
        self.drawPlayer(game.player2, self.player2color)

        #grid
        self.drawGrid(self.player1color if game.turn=="player1" else self.player2color)
