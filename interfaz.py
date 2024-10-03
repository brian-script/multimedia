import yt_dlp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class Interfaz(App):
    def build(self):
        float_body = FloatLayout()
        
        anchor_body = AnchorLayout(anchor_x = "center", anchor_y = "center")

        body = BoxLayout(orientation = "vertical", size_hint = (0.8, None), height = 100)

        body.center_x = float_body.center_x
        body.center_y = float_body.center_y

        titulo = Label(text = "No Name")        
        campo_texto = TextInput(multiline = False, size_hint = (0.8, None), height = 40)

        body.add_widget(titulo)
        body.add_widget(campo_texto)
        
        anchor_body.add_widget(body)
        float_body.add_widget(anchor_body)
        return float_body



if __name__ == "__main__":
    Interfaz().run()
