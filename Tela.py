import PySimpleGUI as sg

class TelaPython():
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Nome'),sg.Input()],
            [sg.Text('Idade'),sg.Input()],
            [sg.Button('Enviar')]
        ]
        #janela
        janela = sg.Window("Dados do usuário").layout(layout)
        #Extrair os dados da tela
        self.button, self.values = janela.Read()
    
    def Iniciar(self):
        print(self.values)

tela = TelaPython()
tela.Iniciar()