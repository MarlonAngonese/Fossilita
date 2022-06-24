from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen

Window.size = (350 , 640)
CURRENT_SCREEN = False;
APP = False;

class Manager(ScreenManager):
    def __init__(self,**kwargs):
        super(Manager,self).__init__(**kwargs)
        #code goes here and add:
        Window.bind(on_keyboard=self.Android_back_click)
    
    def Android_back_click(self,window,key,*largs):
        global APP
        global CURRENT_SCREEN
        if key == 27:

            if (APP.screenmanager.current == 'home'):
                return True

            if (APP.screenmanager.current == 'calculo_de_volume' or APP.screenmanager.current == 'filtro_anaerobio' or APP.screenmanager.current == "sumidouro" or APP.screenmanager.current == 'informacoes_importantes'):
                APP.screenmanager.current = 'home'
                APP.screenmanager.transition.direction = "right"
                return True

            if (APP.screenmanager.current == 'tipo_de_edificacao'):
                APP.tipo_de_edificacao_return_to()
                return True

            if (APP.screenmanager.current == 'resultado_fossa'):
                APP.return_right_to('calculo_de_volume')
                return True

            if (APP.screenmanager.current == 'resultado_filtro_anaerobio'):
                APP.return_right_to('filtro_anaerobio')
                return True

            if (APP.screenmanager.current == 'resultado_sumidouro'):
                APP.return_right_to('sumidouro')
                return True

            if (APP.screenmanager.current == 'intervalo_de_limpeza' or APP.screenmanager.current == 'funcionamento_tanque_septico' or APP.screenmanager.current == 'dimensionamento_tanque_septico' or APP.screenmanager.current == 'dimensionamento_vala_infiltracao' or APP.screenmanager.current == 'tipos_sumidouros' or APP.screenmanager.current == 'manual_boas_praticas'):
                APP.return_right_to('informacoes_importantes')
                return True

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

class ResultadoFiltroAnaerobioScreen(MDScreen):
    pass

class ResultadoSumidouroScreen(MDScreen):
    pass

class FiltroAnaerobioScreen(MDScreen):
    pass

class SumidouroScreen(MDScreen):
    pass
# PDFS
class IntervaloDeLimpezaScreen(MDScreen):
    pass

class FuncionamentoDoTanqueSepticoScreen(MDScreen):
    pass

class DimensionamentoDeTanqueSepticoScreen(MDScreen):
    pass

class DimensionamentoDaValaDeInfiltracaoScreen(MDScreen):
    pass

class TiposDeSumidouroScreen(MDScreen):
    pass

class ManualDeBoasPraticasScreen(MDScreen):
    pass
class Fossilita(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  
        self.screenmanager = Builder.load_file('./main.kv')
        
        global APP
        APP = self

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = '900'
        return self.screenmanager

    def clear_all(self):
        # Fossa
        self.screenmanager.get_screen('calculo_de_volume').ids.dropdown_tipo_de_edificacao.text = "Selecione uma opção"
        self.screenmanager.get_screen('calculo_de_volume').ids.textbox_numero_de_pessoas.text = ""
        self.screenmanager.get_screen('calculo_de_volume').ids.textbox_temperatura_media.text = ""
        self.screenmanager.get_screen('calculo_de_volume').ids.textbox_intervalo_limpeza.text = ""

        self.screenmanager.get_screen('calculo_de_volume').ids.dropdown_tipo_de_edificacao.error = False
        self.screenmanager.get_screen('calculo_de_volume').ids.textbox_numero_de_pessoas.error = False
        self.screenmanager.get_screen('calculo_de_volume').ids.textbox_temperatura_media.error = False
        self.screenmanager.get_screen('calculo_de_volume').ids.textbox_intervalo_limpeza.error = False

        # Filtro Anaeróbio
        self.screenmanager.get_screen('filtro_anaerobio').ids.dropdown_tipo_de_edificacao.text = "Selecione uma opção"
        self.screenmanager.get_screen('filtro_anaerobio').ids.textbox_numero_de_pessoas.text = ""

        self.screenmanager.get_screen('filtro_anaerobio').ids.dropdown_tipo_de_edificacao.error = False
        self.screenmanager.get_screen('filtro_anaerobio').ids.textbox_numero_de_pessoas.error = False

        # Sumidouro/Vala de Infiltração
        self.screenmanager.get_screen('sumidouro').ids.dropdown_tipo_de_edificacao.text = "Selecione uma opção"
        self.screenmanager.get_screen('sumidouro').ids.textbox_numero_de_pessoas.text = ""
        self.screenmanager.get_screen('sumidouro').ids.textbox_coeficiente_percolacao.text = ""
        
        self.screenmanager.get_screen('sumidouro').ids.dropdown_tipo_de_edificacao.error = False
        self.screenmanager.get_screen('sumidouro').ids.textbox_numero_de_pessoas.error = False
        self.screenmanager.get_screen('sumidouro').ids.textbox_coeficiente_percolacao.error = False
    
    def change_tipo_de_edificacao_screen(self, screen):
        global CURRENT_SCREEN

        self.screenmanager.current = "tipo_de_edificacao"
        self.screenmanager.transition.direction = "left"

        self.screenmanager.get_screen('tipo_de_edificacao').ids.tipo_de_edificacao_scrollview.size = (Window.width, Window.height - Window.height * 0.27)

        CURRENT_SCREEN = screen
        global APP
        APP = self

    def choose_option_tipo_de_edificacao(self, option):
        global CURRENT_SCREEN

        self.screenmanager.current = CURRENT_SCREEN
        self.screenmanager.transition.direction = "right"

        self.screenmanager.get_screen(CURRENT_SCREEN).ids.dropdown_tipo_de_edificacao.text = option.text

        if (option.text == "Restaurantes e Similares" or option.text == "Bares"):
            self.screenmanager.get_screen(CURRENT_SCREEN).ids.label_numero_de.text = "Número de Refeições"
        elif (option.text == "Cinemas, Teatros e Locais de Curta Permanência"):
            self.screenmanager.get_screen(CURRENT_SCREEN).ids.label_numero_de.text = "Número de Lugares"
        elif (option.text == "Sanitários Públicos"):
            self.screenmanager.get_screen(CURRENT_SCREEN).ids.label_numero_de.text = "Número de Bacias Sanitárias"
        else:
            self.screenmanager.get_screen(CURRENT_SCREEN).ids.label_numero_de.text = "Número de Pessoas"

        global APP
        APP = self

    def tipo_de_edificacao_return_to(self):
        global CURRENT_SCREEN
        self.screenmanager.current = CURRENT_SCREEN
        self.screenmanager.transition.direction = "right"

        global APP
        APP = self

    def return_to_home(self):
        self.screenmanager.current = "home"
        self.screenmanager.transition.direction = "right"

        self.clear_all()

        global APP
        APP = self

    def return_right_to(self, target):
        self.screenmanager.current = target
        self.screenmanager.transition.direction = "right"

        if (target == "home"):
            self.clear_all()

        global APP
        APP = self

    def return_left_to(self, target):
        self.screenmanager.current = target
        self.screenmanager.transition.direction = "left"

        global APP
        APP = self

    def change_information_screen(self, screen):
        self.screenmanager.current = screen
        self.screenmanager.transition.direction = "left"

        self.screenmanager.get_screen(screen).ids.scrollview.size = (Window.width, Window.height - Window.height * 0.27)

        global APP
        APP = self

    def calculate_volume_util(self):
        if (self.screenmanager.get_screen('calculo_de_volume').ids.dropdown_tipo_de_edificacao.text != "Selecione uma opção"):
            Edificacao = self.screenmanager.get_screen('calculo_de_volume').ids.dropdown_tipo_de_edificacao.text # Tipo de Edificação
        else:
            self.screenmanager.get_screen('calculo_de_volume').ids.dropdown_tipo_de_edificacao.error = True
            return

        if (self.screenmanager.get_screen('calculo_de_volume').ids.textbox_numero_de_pessoas.text != ""):
            Np = int(self.screenmanager.get_screen('calculo_de_volume').ids.textbox_numero_de_pessoas.text) # Número de Pessoas
        else:
            self.screenmanager.get_screen('calculo_de_volume').ids.textbox_numero_de_pessoas.error = True
            return

        if (self.screenmanager.get_screen('calculo_de_volume').ids.textbox_temperatura_media.text != ""):
            Temperatura_media = int(self.screenmanager.get_screen('calculo_de_volume').ids.textbox_temperatura_media.text)  # Temperatura Média
        else:
            self.screenmanager.get_screen('calculo_de_volume').ids.textbox_temperatura_media.error = True
            return

        if (self.screenmanager.get_screen('calculo_de_volume').ids.textbox_intervalo_limpeza.text != ""):
            Intervalo_limpeza = int(self.screenmanager.get_screen('calculo_de_volume').ids.textbox_intervalo_limpeza.text) # Intervalo de Limpeza
        else:
            self.screenmanager.get_screen('calculo_de_volume').ids.textbox_intervalo_limpeza.error = True
            return

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
            T = 1
        elif (Cd >= 1501 and Cd <= 3000):
            T = 0.92
        elif (Cd >= 3001 and Cd <= 4500):
            T = 0.83
        elif (Cd >= 4501 and Cd <= 6000):
            T = 0.75
        elif (Cd >= 6001 and Cd <= 7500):
            T = 0.67
        elif (Cd >= 7501 and Cd <= 9000):
            T = 0.58
        elif (Cd >= 9001):
            T = 0.5

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

        Volume_util = round(1000 + Np * (C * T + K * Lf), 2)

        self.screenmanager.current = "resultado_fossa"
        self.screenmanager.transition.direction = "left"

        self.screenmanager.get_screen('resultado_fossa').ids.label_resultado_fossa.text = f'{Volume_util} litros'

        global APP
        APP = self

    def calculate_filtro_anaerobio(self):

        if (self.screenmanager.get_screen('filtro_anaerobio').ids.dropdown_tipo_de_edificacao.text != "Selecione uma opção"):
            Edificacao = self.screenmanager.get_screen('filtro_anaerobio').ids.dropdown_tipo_de_edificacao.text # Tipo de Edificação
        else:
             self.screenmanager.get_screen('filtro_anaerobio').ids.dropdown_tipo_de_edificacao.error = True
             return

        if (self.screenmanager.get_screen('filtro_anaerobio').ids.textbox_numero_de_pessoas.text != ""):
            Np = int(self.screenmanager.get_screen('filtro_anaerobio').ids.textbox_numero_de_pessoas.text) # Número de Pessoas
        else:
            self.screenmanager.get_screen('filtro_anaerobio').ids.textbox_numero_de_pessoas.error = True
            return

        C = False

        if(Edificacao == "Residência"):
            C = 200

        elif(Edificacao == "Alojamento Provisório"):
            C = 80

        elif(Edificacao == "Fábrica em Geral"):
            C = 70

        elif(Edificacao == "Escritório"):
            C = 50

        elif(Edificacao == "Edifícios Públicos ou Comerciais"):
            C = 50

        elif(Edificacao == "Escolas ou Locais de Longa Permanência"):
            C = 50

        elif(Edificacao == "Bares"):
            C = 6

        elif(Edificacao == "Restaurantes e Similares"):
            C = 25

        elif(Edificacao == "Cinemas, Teatros e Locais de Curta Permanência"):
            C = 2

        elif(Edificacao == "Sanitários Públicos"):
            C = 480

        Cd = C * Np

        if (Cd <= 1500):
            T = 1

        elif (Cd >= 1501 and Cd <= 3000):
            T = 0.92

        elif (Cd >= 3001 and Cd <= 4500):
            T = 0.83

        elif (Cd >= 4501 and Cd <= 6000):
            T = 0.75

        elif (Cd >= 6001 and Cd <= 7500):
            T = 0.67

        elif (Cd >= 7501 and Cd <= 9000):
            T = 0.58

        elif (Cd >= 9001):
            T = 0.5

        Volume_util = round(1.60  * Np * C * T, 2)

        Volume_cubico = round(Volume_util / 1000, 2)
        Secao_horizontal = round(Volume_cubico/1.80, 2)

        self.screenmanager.current = "resultado_filtro_anaerobio"
        self.screenmanager.transition.direction = "left"

        self.screenmanager.get_screen('resultado_filtro_anaerobio').ids.label_resultado_filtro_anaerobio.text = f'{Volume_util} litros'

        self.screenmanager.get_screen('resultado_filtro_anaerobio').ids.label_resultado_secao_horizontal.text = f'{Secao_horizontal} m²'

        global APP
        APP = self

    def calculate_sumidouro(self):
        if (self.screenmanager.get_screen('sumidouro').ids.dropdown_tipo_de_edificacao.text != "Selecione uma opção"):
            Edificacao = self.screenmanager.get_screen('sumidouro').ids.dropdown_tipo_de_edificacao.text # Tipo de Edificação
        else:
            self.screenmanager.get_screen('sumidouro').ids.dropdown_tipo_de_edificacao.error = True
            return

        if (self.screenmanager.get_screen('sumidouro').ids.textbox_numero_de_pessoas.text != ""):
            Np = int(self.screenmanager.get_screen('sumidouro').ids.textbox_numero_de_pessoas.text) # Número de Pessoas
        else:
            self.screenmanager.get_screen('sumidouro').ids.textbox_numero_de_pessoas.error = True
            return

        if (self.screenmanager.get_screen('sumidouro').ids.textbox_coeficiente_percolacao.text != ""):
            Ci = float(self.screenmanager.get_screen('sumidouro').ids.textbox_coeficiente_percolacao.text) # Coeficiente de Percolação
        else:
            self.screenmanager.get_screen('sumidouro').ids.textbox_coeficiente_percolacao.error = True
            return

        C = False

        if(Edificacao == "Residência"):
            C = 200

        elif(Edificacao == "Alojamento Provisório"):
            C = 80

        elif(Edificacao == "Fábrica em Geral"):
            C = 70

        elif(Edificacao == "Escritório"):
            C = 50

        elif(Edificacao == "Edifícios Públicos ou Comerciais"):
            C = 50

        elif(Edificacao == "Escolas ou Locais de Longa Permanência"):
            C = 50

        elif(Edificacao == "Bares"):
            C = 6

        elif(Edificacao == "Restaurantes e Similares"):
            C = 25

        elif(Edificacao == "Cinemas, Teatros e Locais de Curta Permanência"):
            C = 2

        elif(Edificacao == "Sanitários Públicos"):
            C = 480

        V = C*Np

        A = round(V/Ci, 2)

        self.screenmanager.current = "resultado_sumidouro"
        self.screenmanager.transition.direction = "left"

        self.screenmanager.get_screen('resultado_sumidouro').ids.label_resultado_area.text = f'{A} m²'

        global APP
        APP = self

Fossilita().run()