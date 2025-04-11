import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1, 0, 0, 1]      
green = [0, 1, 0, 1]    
blue = [0, 0, 1, 1]     
purple = [1, 0, 1, 1]  

class VBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(
            orientation='vertical',
            padding=[30, 50, 30, 20],
            spacing=20
        )

        colors = [red, green, blue, purple]
        for i, color in enumerate(colors):
            btn = Button(
                text=f"Кнопка {i+1}",
                background_color=color,
                size_hint=(0.8, None),  # Ширина 80%, высота не автоматическая
                height=100,             # Фиксированная высота 100px
                pos_hint={'center_x': 0.5}  # Центрирование по горизонтали
            )
            layout.add_widget(btn)

        return layout

if __name__ == "__main__":
    VBoxLayoutExample().run()
