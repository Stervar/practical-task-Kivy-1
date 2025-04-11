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
 
        # padding=[слева, сверху, справа, снизу]
        layout = BoxLayout(
            orientation='vertical',
            padding=[30, 50, 30, 20],  # Отступы: слева 30, сверху 50, справа 30, снизу 20
            spacing=20                  # Расстояние между кнопками
        )

        colors = [red, green, blue, purple]

        for i, color in enumerate(colors):
            btn = Button(
                text=f"Кнопка {i+1}",
                background_color=color,
                size_hint=(1, 0.2)  # Ширина 100%, высота 20% от layout
            )
            layout.add_widget(btn)

        return layout

if __name__ == "__main__":
    VBoxLayoutExample().run()






# padding: Отступ padding между лейаутом и его дочерними элементами уточняется в пикселях. Для этого можно выбрать один из трех способов:
    
# Список из четырех аргументов: [padding_left, padding_top, padding_right, padding_bottom]

# Список из двух аргументов: [padding_horizontal, padding_vertical]

# Один аргумент: padding=10

# spacing: При помощи данного аргумента добавляется расстояние между дочерними виджетами.

# orientation: Позволяет изменить значение orientation для BoxLayout по умолчанию — с горизонтального на вертикальное.