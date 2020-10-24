import PySimpleGUI as sg  

class Window:
    def __init__(self):
            pass
    def playerType(self):
        layout = [  
            [sg.Text("VOCÊ É SERVER OU CLIENT?")],     # Part 2 - The Layout
            [sg.Button('Server')], [sg.Button('Client')] ]
        # Create the window
        window = sg.Window('TRON TCP', layout)

        # Display and interact with the Window
        teste=""
        event, values = window.read()    
        if(event == 'Server'):
            teste='s'
        elif(event == 'Client'):
            teste='c'
        
        window.close()    
        return(teste)  

    def showPort(self, port):
        layout = [  
            [sg.Text("PASSE ESSA PORTA PARA SEU COLEGA")],     # Part 2 - The Layout
            [sg.Text(port)],
            [sg.Button('OK')]]

        window = sg.Window('TRON TCP', layout)
        # Display and interact with the Window
        event, values = window.read()    

        if(event == 'OK'):
            window.close() 

    def askPort(self):
        layout = [  
            [sg.Text("QUAL O ENDEREÇO E PORTA DO SEU COLEGA?")],
            [sg.Text("deixe em branco caso localhost")],     # Part 2 - The Layout
            [sg.Input(key='ENDEREÇO')],
            [sg.Input(key='PORTA'), sg.Button('OK')]]
        window = sg.Window('TRON TCP', layout)
        event, values = window.read()    

        if(event == 'OK'):
            window.close()
            return values['ENDEREÇO'], values['PORTA']
    
    def endGame(self, winner):
        layout = [  
            [sg.Text(f"{winner} venceu!!!")],
            [sg.Button('OK')]]
        window = sg.Window('TRON TCP', layout)
        event, values = window.read()
        if(event == 'OK'):
            window.close()
            return False

    def showColor(self,color):
        layout = [  
            [sg.Text(f"voce é o {color}")],
            [sg.Button('OK')]]
        window = sg.Window('TRON TCP', layout)
        event, values = window.read()
        if(event == 'OK'):
            window.close()

# wind =Window()
# a,b = wind.askPort()
# print(a=="")