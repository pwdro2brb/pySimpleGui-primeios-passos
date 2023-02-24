import PySimpleGUI as sg

class TelaPython():
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(20,0),key='Nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(20,0),key='Idade')],# key = identificação dos valores exmplo outlook ao invês de aparecer como "3" ele vai aparecer como "outlook"
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key='Gmail'),sg.Checkbox('Outlook',key='Outlook'),sg.Checkbox("Yahoo",key='Yahoo')],
            [sg.Text('Aceita cartão?')],
            [sg.Radio('sim','cartões',key='aceitaCartao'),sg.Radio('Não','cartões',key='naoAceitaCartao')],
            [sg.Button('Enviar')]
        ]
        #janela
        janela = sg.Window("Dados do usuário").layout(layout)
        #Extrair os dados da tela
        self.button, self.values = janela.Read()
    
    def Iniciar(self):
        nome = self.values['Nome']
        idade = self.values['Idade']
        g_mail = self.values['Gmail']
        ou_tlook = self.values['Outlook']
        ya_hoo = self.values['Yahoo']
        aceita_cartão_sim = self.values['aceitaCartao']
        nao_aceita_cartão = self.values['naoAceitaCartao']
        print(f'Nome:{nome}')
        print(f'Idade:{idade}')
        print(f'Gmail:{g_mail}')
        print(f'Outlook:{ou_tlook}')
        print(f'Yahoo:{ya_hoo}')
        print(f'aceitaCartao:{aceita_cartão_sim}')
        print(f'naoAceitaCartao:{nao_aceita_cartão}')


tela = TelaPython()
tela.Iniciar()