import PySimpleGUI as sg

class TelaPython():
    def __init__(self):
        sg.change_look_and_feel('DarkTeal11')#Troca o thema de fundo da tela. Também utilize deste link para mais themas de cores https://www.geeksforgeeks.org/themes-in-pysimplegui/
        #layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(20,0),key='Nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(20,0),key='Idade')],# key = identificação dos valores exmplo outlook ao invês de aparecer como "3" ele vai aparecer como "outlook"
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key='Gmail'),sg.Checkbox('Outlook',key='Outlook'),sg.Checkbox("Yahoo",key='Yahoo')],
            [sg.Text('Aceita cartão?')],
            [sg.Radio('sim','cartões',key='Aceita Cartão'),sg.Radio('Não','cartões',key='Não Aceita Cartão')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')],
            [sg.Button('Enviar')],
            [sg.Output(size=(30,20))]#gera a informação na tela sem ir no terminal 
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
          velocidade_script = self.values['sliderVelocidade']
          print(f'Nome:{nome}')
          print(f'Idade:{idade}')
          print(f'Gmail:{g_mail}')
          print(f'Outlook:{ou_tlook}')
          print(f'Yahoo:{ya_hoo}')
          print(f'Aceita Cartão:{aceita_cartão_sim}')
          print(f'Não Aceita Cartâo:{nao_aceita_cartão}')
          print(f'Velocidade Scrits: {velocidade_script}')


tela = TelaPython()
tela.Iniciar()

