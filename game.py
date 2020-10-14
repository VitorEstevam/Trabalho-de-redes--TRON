class Game:
    up=273
    right=275
    down=274
    left=276

    turn="player1"

    running = True
    winner="no one"

    def __init__(self):
        self.player1={"x":1,"y":1}
        self.player2={"x":5,"y":5}

        self.player1Tail=[]
        self.player2Tail=[]
    
    def moveplayer1(self,direction):
        pos={'x':self.player1['x'], "y":self.player1['y']}
        
        if(direction== self.left and self.player1["x"]>0):
            self.player1["x"]-= 1
        elif(direction== self.right and self.player1["x"]<9):
            self.player1["x"]+=1
        elif(direction== self.up and self.player1["y"]>0):
            self.player1["y"]-=1
        elif(direction==  self.down and self.player1["y"]<9):
            self.player1["y"]+=1
        else:
            return

        if(pos not in self.player1Tail):
            self.player1Tail.append(pos)
        print(self.player1Tail)

        self.turn="player2"


    def moveplayer2(self,direction):
        pos={'x':self.player2['x'], "y":self.player2['y']}
        
        if(direction== self.left and self.player2["x"]>0):
            self.player2["x"]-=1
        elif(direction== self.right and self.player2["x"]<9):
            self.player2["x"]+=1
        elif(direction== self.up and self.player2["y"]>0):
            self.player2["y"]-=1
        elif(direction==  self.down and self.player2["y"]<9):
            self.player2["y"]+=1
        else:
            return

        if(pos not in self.player2Tail):
            self.player2Tail.append(pos)
        print(self.player2Tail)

        self.turn="player1"

    def checkPlayerOverTail(self):
        if(self.player1 in self.player1Tail or self.player1 in self.player2Tail):
            print("player 1 hitted line")
            self.winner="player2"
            self.running=False

        if(self.player2 in self.player1Tail or self.player2 in self.player2Tail):
            print("player 2 hitted line")
            self.winner="player1"
            self.running=False