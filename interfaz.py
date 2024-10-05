from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
import logica

class Interfaz(App):
    def build(self):
        float_body = FloatLayout()
        
        anchor_body = AnchorLayout(anchor_x = "center", anchor_y = "center")

        body = BoxLayout(orientation = "vertical", size_hint = (0.8, None), height = 100)

        body.center_x = float_body.center_x
        body.center_y = float_body.center_y

        titulo = Label(text = "No Name")        
        self.campo_texto = TextInput(multiline = False, height = 40)
        self.campo_texto.bind(on_text_validate = self.enviardatos)

        # Crear el Dropdown
        self.dropdown = DropDown()

        # Opción 1
        self.option1 = Button(text='Opción 1', size_hint_y=None, height=44)
        self.option1.bind(on_release=self.opciones)
        self.dropdown.add_widget(self.option1)

        # Opción 2
        self.option2 = Button(text='Opción 2', size_hint_y=None, height=44)
        self.option2.bind(on_release=self.opciones)
        self.dropdown.add_widget(self.option2)

        # Botón que mostrará el Dropdown
        self.dropdown_button = Button(text='Selecciona una opción', size_hint=(None, None), height=44)
        self.dropdown_button.bind(on_release=self.dropdown.open)

        # Agregar los widgets al layout
        body.add_widget(titulo)
        body.add_widget(self.campo_texto)
        body.add_widget(self.dropdown_button)  # Agregar el botón que mostrará el dropdown
        
        anchor_body.add_widget(body)
        float_body.add_widget(anchor_body)
        return float_body

    def enviardatos(self, instance):
        link = self.campo_texto.text
        logica.download_mp4(link)

    def opciones(self, instance):
        # Aquí puedes manejar lo que debe ocurrir cuando se seleccione una opción
        if instance.text == "Opción 1":
            print("Seleccionaste Opción 1")
        elif instance.text == "Opción 2":
            print("Seleccionaste Opción 2")
        self.dropdown.dismiss()  # Cerrar el dropdown después de seleccionar

if __name__ == "__main__":
    Interfaz().run()

