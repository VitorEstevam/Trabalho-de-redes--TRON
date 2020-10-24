import socket as socket
import pickle
from game import Game

class MySocket:
    def __init__(self,port=1234):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket = None
        self.port=port

    def server(self) :
        print("opening server")
        self.serverSocket.bind((socket.gethostname(), self.port))

    def clientConnect(self, port, host=socket.gethostname()):
        self.serverSocket.connect((host, port))
        msg = self.serverSocket.recv(1024)
        print(msg.decode('utf-8'))

    def serverConnect(self):
        self.serverSocket.listen(5)
        print("waiting connection")
        self.clientsocket, address = self.serverSocket.accept()
        print(f"access from {address}")
        self.clientsocket.send(bytes("connected ;)","utf-8"))


    def send(self,message):
        if(self.clientsocket is not None):#server
            print('SERVER SENDING==>')
            self.clientsocket.send(bytes(message,"utf-8"))
        elif(self.clientsocket is None):#client
            print('CLIENT SENDING==>')
            self.serverSocket.send(bytes(message,"utf-8"))

    def receive(self):
        if(self.clientsocket is not None):#server
            print('SERVER RECEIVING<==')
            msg = self.clientsocket.recv(1024)
            return msg.decode('utf-8')

        elif(self.clientsocket is None):#client
            print('CLIENT RECEIVING<==')
            msg = self.serverSocket.recv(1024)
        return msg.decode('utf-8')

    def sendGame(self,game):
        dict = game.__dict__
        dict_str=pickle.dumps(dict)
        # print(dict_str)

        if(self.clientsocket is not None):#server
            print('SERVER SENDING game==>')
            self.clientsocket.send(dict_str)
        elif(self.clientsocket is None):#client
            print('CLIENT SENDING game==>')
            self.serverSocket.send(dict_str)


    def receiveGame(self):
        if(self.clientsocket is not None):#server
            print('SERVER RECEIVING game<==')
            msg = self.clientsocket.recv(1024)

        elif(self.clientsocket is None):#client
            print('CLIENT RECEIVING game<==')
            msg = self.serverSocket.recv(1024)

        dict=pickle.loads(msg)

        classAux=Game()

        for name,content in dict.items():
            setattr(classAux,name,content)

        return(classAux)
