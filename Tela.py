import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.text('Nome'),sg.Input()],
            [sg.Text('Idade'),sg.Input()],
            [sg.Button]
        ]
        #janela
        janela = sg.window("Dados do usuário").layout(layout)