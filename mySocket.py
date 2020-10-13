import socket as socket

class MySocket:
    def __init__(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket = None
    def server(self, port=1234):
        print("abrindo server")
        self.serverSocket.bind((socket.gethostname(), port))

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


test=MySocket()
enter=input("S or C\n")

if(enter in ["s","S"]):
    test.server()
    test.serverConnect()

    test.send("bom dia")
    print(test.receive())

elif(enter in ["c","C"]):
    test.clientConnect(1234)
    print(test.receive())
    test.send("boa noite")