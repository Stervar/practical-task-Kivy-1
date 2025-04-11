import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=100, spacing=10, orientation='vertical')
        colors = [red, green, blue, purple]
        padding_vertical
        for i, color in enumerate(colors):
            btn = Button(text=f"Color {i+1}",
                         background_color=color
                         )
            layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    app = HBoxLayoutExample()
    app.run()
    
    
#     padding: Отступ padding между лейаутом и его дочерними элементами уточняется в пикселях. Для этого можно выбрать один из трех способов:
        
# Список из четырех аргументов: [padding_left, padding_top, padding_right, padding_bottom]

# Список из двух аргументов: [padding_horizontal, padding_vertical]

# Один аргумент: padding=10

# spacing: При помощи данного аргумента добавляется расстояние между дочерними виджетами.

# orientation: Позволяет изменить значение orientation для BoxLayout по умолчанию — с горизонтального на вертикальное.