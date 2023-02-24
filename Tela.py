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
            [sg.Radio('sim','cartões',key='Aceita Cartão'),sg.Radio('Não','cartões',key='Não Aceita Cartão')],
            [sg.Button('Enviar')]
        ]
        #janela
        self.janela = sg.Window("Dados do usuário").layout(layout)


    
    def Iniciar(self):
        while True: 
          #Extrair os dados da tela
          self.button, self.values = self.janela.Read()
          nome = self.values['Nome']
          idade = self.values['Idade']
          g_mail = self.values['Gmail']
          ou_tlook = self.values['Outlook']
          ya_hoo = self.values['Yahoo']
          aceita_cartão_sim = self.values['Aceita Cartão']
          nao_aceita_cartão = self.values['Não Aceita Cartão']
          print(f'Nome:{nome}')
          print(f'Idade:{idade}')
          print(f'Gmail:{g_mail}')
          print(f'Outlook:{ou_tlook}')
          print(f'Yahoo:{ya_hoo}')
          print(f'Aceita Cartão:{aceita_cartão_sim}')
          print(f'Não Aceita Cartâo:{nao_aceita_cartão}')


tela = TelaPython()
tela.Iniciar()