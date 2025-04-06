from kivy.app import App
from kivy.uix.image import Image
import os

class MainApp(App):
    def build(self):
        # Использовали абсолютный путь к картинке
        img_path = os.path.join(os.path.dirname(__file__), 'image', 'Load-Image-Kivy.png')
        img = Image(source=img_path,
                   size_hint=(1, .5),
                   pos_hint={'center_x':.5, 'center_y':.5})
        return img

if __name__ == '__main__':
    MainApp().run()
