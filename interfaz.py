from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
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
        enviar = Button(text = "Enviar", background_color = "red")

        body.add_widget(titulo)
        body.add_widget(self.campo_texto)
        body.add_widget(enviar)
        
        anchor_body.add_widget(body)
        float_body.add_widget(anchor_body)
        return float_body

    def enviardatos(self, instance):
        link = self.campo_texto.text
        logica.download_mp4(link)

if __name__ == "__main__":
    Interfaz().run()
