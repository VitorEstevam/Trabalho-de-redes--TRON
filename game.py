class Game:
    up=273
    right=275
    down=274
    left=276

    def __init__(self):
        self.player1={"x":1,"y":1}
        self.player2={"x":5,"y":5}

        self.player1Tail=[]
    
    def moveplayer1(self,direction):
        pos={'x':self.player1['x'], "y":self.player1['y']}
        if(pos not in self.player1Tail):
            self.player1Tail.append(pos)
        print(self.player1Tail)

        if(direction== self.left):
            self.player1["x"]-=1
        elif(direction== self.right):
            self.player1["x"]+=1
        elif(direction== self.up):
            self.player1["y"]-=1
        elif(direction==  self.down):
            self.player1["y"]+=1


    # def moveplayer2(self,direction):
    #     if(direction== "left"):
    #         self.player2.x-=1
    #     elif(direction== "right"):
    #         self.player2.x+=1
    #     elif(direction==  "up"):
    #         self.player2.y-=1
    #     elif(direction==  "down"):
    #         self.player2.y+=1