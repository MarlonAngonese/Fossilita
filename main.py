from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu

from fossilita import Intervalo_limpeza

Window.size = (350 , 640)

class Manager(ScreenManager):
    pass

class InformacoesImportantesScreen(MDScreen):
    pass

class CalculoDeVolumeScreen(MDScreen):
    pass

class HomeScreen(MDScreen):
    pass

class TipoDeEdificacaoScreen(MDScreen):
    pass

class ResultadoFossaScreen(MDScreen):
    pass

class Fossilita(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.screenmanager = Builder.load_file('./main.kv')

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = '900'
        return self.screenmanager
    
    def change_tipo_de_edificacao_screen(self):
        self.screenmanager.current = "tipo_de_edificacao"
        self.screenmanager.transition.direction = "left"

        self.screenmanager.get_screen('tipo_de_edificacao').ids.tipo_de_edificacao_scrollview.size = (Window.width, Window.height)

    def return_to_home(self):
        self.screenmanager.current = "home"
        self.screenmanager.transition.direction = "right"

    def return_right_to(self, target):
        self.screenmanager.current = target
        self.screenmanager.transition.direction = "right"

    def return_left_to(self, target):
        self.screenmanager.current = target
        self.screenmanager.transition.direction = "left"

    def calculate_volume_util(self):
        Edificacao = self.screenmanager.get_screen('calculo_de_volume').ids.dropdown_tipo_de_edificacao.text # Tipo de Edificação
        Np = int(self.screenmanager.get_screen('calculo_de_volume').ids.textbox_numero_de_pessoas.text) # Número de Pessoas
        Temperatura_media = int(self.screenmanager.get_screen('calculo_de_volume').ids.textbox_temperatura_media.text)  # Temperatura Média
        Intervalo_limpeza = int(self.screenmanager.get_screen('calculo_de_volume').ids.textbox_intervalo_limpeza.text) # Intervalo de Limpeza

        C = False #Contribuição de Esgoto por Unidade
        T = False #Tempo de detenção
        Lf = False #Contribuição de Lodo Fresco
        Cd = False #Contribuição Diária
        K = False #Taxa de acumulação de Lodo Fresco

        if (Edificacao == "Residência"):
            C = 200
            Lf = 1
        elif (Edificacao == "Alojamento Provisório"):
            C = 80
            Lf = 1
        elif (Edificacao == "Fábrica em Geral"):
            C = 70
            Lf = 0.3
        elif (Edificacao == "Escritório"):
            C = 50
            Lf = 0.2
        elif (Edificacao == "Edifícios Públicos ou Comerciais"):
            C = 50
            Lf = 0.2
        elif (Edificacao == "Escolas ou Locais de Longa Permanência"):
            C = 50
            Lf = 0.2
        elif (Edificacao == "Bares"):
            C = 6
            Lf = 0.1
        elif (Edificacao == "Restaurantes e Similares"):
            C = 25
            Lf = 0.1
        elif (Edificacao == "Cinemas, Teatros e Locais de Curta Permanência"):
            C = 2
            Lf = 0.02
        elif (Edificacao == "Sanitários Públicos"):
            C = 480
            Lf = 4

        Cd = Np * C  #Cálculo da Contribuição Diária

        if (Cd <= 1500):
            T = 24
        elif (Cd >= 1501 and Cd <= 3000):
            T = 22
        elif (Cd >= 3001 and Cd <= 4500):
            T = 20
        elif (Cd >= 4501 and Cd <= 6000):
            T = 18
        elif (Cd >= 6001 and Cd <= 7500):
            T = 16
        elif (Cd >= 7501 and Cd <= 9000):
            T = 14
        elif (Cd >= 9001):
            T = 12

        if (Temperatura_media < 10 and Intervalo_limpeza == 1):
            K = 94

        elif (Temperatura_media < 10 and Intervalo_limpeza == 2):
            K = 134

        elif (Temperatura_media < 10 and Intervalo_limpeza == 3):
            K = 174

        elif (Temperatura_media < 10 and Intervalo_limpeza == 4):
            K = 214

        elif (Temperatura_media < 10 and Intervalo_limpeza == 5):
            K = 254

        elif (Temperatura_media >= 11 and Temperatura_media <= 20 and Intervalo_limpeza == 1):
            K = 65

        elif (Temperatura_media >= 11 and Temperatura_media <= 20 and Intervalo_limpeza == 2):
            K = 105

        elif (Temperatura_media >= 11 and Temperatura_media <= 20 and Intervalo_limpeza == 3):
            K = 145

        elif (Temperatura_media >= 11 and Temperatura_media <= 20 and Intervalo_limpeza == 4):
            K = 185

        elif (Temperatura_media >= 11 and Temperatura_media <= 20 and Intervalo_limpeza == 5):
            K = 225


        elif (Temperatura_media >= 21 and Intervalo_limpeza == 1):
            K = 57

        elif (Temperatura_media >= 21 and Intervalo_limpeza == 2):
            K = 97

        elif (Temperatura_media >= 21 and Intervalo_limpeza == 3):
            K = 137

        elif (Temperatura_media >= 21 and Intervalo_limpeza == 4):
            K = 177

        elif (Temperatura_media >= 21 and Intervalo_limpeza == 5):
            K = 217

        Volume_util = round(float(1000 + Np * (C * T + K + Lf)), 2)

        self.screenmanager.current = "resultado_fossa"
        self.screenmanager.transition.direction = "left"

        self.screenmanager.get_screen('resultado_fossa').ids.label_resultado_fossa.text = f'{Volume_util} litros'

    def choose_option_tipo_de_edificacao(self, option):
        self.screenmanager.current = "calculo_de_volume"
        self.screenmanager.transition.direction = "right"

        self.screenmanager.get_screen('calculo_de_volume').ids.dropdown_tipo_de_edificacao.text = option.text

        if (option.text == "Restaurantes e Similares" or option.text == "Bares"):
            self.screenmanager.get_screen('calculo_de_volume').ids.label_numero_de.text = "Número de Refeições"
        elif (option.text == "Cinemas, Teatros e Locais de Curta Permanência"):
            self.screenmanager.get_screen('calculo_de_volume').ids.label_numero_de.text = "Número de Lugares"
        elif (option.text == "Sanitários Públicos"):
            self.screenmanager.get_screen('calculo_de_volume').ids.label_numero_de.text = "Número de Bacias Sanitárias"
        else:
            self.screenmanager.get_screen('calculo_de_volume').ids.label_numero_de.text = "Número de Pessoas"

Fossilita().run()