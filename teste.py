from mySocket import MySocket
from game import Game



game=Game()

test=MySocket()
enter=input("S or C\n")
if(enter in ["s","S"]):
    test.server()
    test.serverConnect()

    game.player1= {'x': 3, 'y': 3}
    test.sendGame(game)
    game=test.receiveGame()

    print(game.__dict__)

elif(enter in ["c","C"]):
    test.clientConnect(1234)
    game=test.receiveGame()

    game.player1= {'x': 5, 'y': 5}
    test.sendGame(game)
    print(game.__dict__)