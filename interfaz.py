from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
import logica

class Interfaz(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.link = ""
        self.selected_option = None


    def build(self):
        #layout principal
        float_body = FloatLayout()

        with float_body.canvas.before:
            Color(0.882, 0.973, 0.980, 0.2)
            self.rect = Rectangle(size = float_body.size, pos = float_body.pos)

        float_body.bind(size = self._update_rect, pos = self._update_rect)

        #layout secundario
        anchor_body = AnchorLayout(anchor_x="center", anchor_y="center")

        #layout tercero
        body = BoxLayout(orientation="vertical", size_hint=(0.8, None), height=100)

        #layuot cuarto
        empaquetador = GridLayout(rows = 1, cols = 2)

        body.center_x = float_body.center_x
        body.center_y = float_body.center_y
        
        #Estos se guardan dentro del tercer layout osea body
        titulo = Label(text="No Name")        
        self.campo_texto = TextInput(multiline=False, height=44, disabled=True, size_hint_x = None, width = 600)
        self.campo_texto.bind(on_text_validate=self.enviardatos)

        # Crear el Dropdown
        self.dropdown = DropDown()

        # Opción 1
        self.option1 = Button(text='Opción 1', size_hint_y=None, height=44)
        self.option1.bind(on_release=self.datos)
        self.dropdown.add_widget(self.option1)

        # Opción 2
        self.option2 = Button(text='Opción 2', size_hint_y=None, height=44)
        self.option2.bind(on_release=self.datos)
        self.dropdown.add_widget(self.option2)

        # Botón que mostrará el Dropdown
        self.dropdown_button = Button(text='Selecciona una opción', size_hint=(None, None), height=44)
        self.dropdown_button.bind(on_release=self.dropdown.open)

        # Agregar los widgets al layout
        empaquetador.add_widget(self.campo_texto)
        empaquetador.add_widget(self.dropdown_button)
        body.add_widget(titulo)
        body.add_widget(empaquetador)
        #body.add_widget(self.dropdown_button)  
        anchor_body.add_widget(body)
        float_body.add_widget(anchor_body)
        return float_body

    def _update_rect(self, *args):
        self.rect.pos = (0,0)
        self.rect.size = self.root.size

    def datos(self, instance):  # Corregido: sefl -> self
        self.selected_option = instance.text
        self.campo_texto.disabled = False  # Habilita el campo de texto
        self.dropdown.dismiss()

    def enviardatos(self, instance):
        self.link = self.campo_texto.text  # Almacena el enlace

        if self.selected_option == "Opción 1":
            logica.download_mp3(self.link)  # Usa self.link
        elif self.selected_option == "Opción 2":
            logica.download_mp4(self.link)  # Usa self.link

        self.campo_texto.text = ""  # Limpia el campo de texto
        self.selected_option = None  # Reinicia la opción seleccionada
        self.campo_texto.disabled = True  # Deshabilita el campo de texto nuevamente

if __name__ == "__main__":
    Interfaz().run()
