import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Цвета в формате RGBA
red = [1, 0, 0, 1]      # Красный
green = [0, 1, 0, 1]    # Зеленый
blue = [0, 0, 1, 1]     # Синий
purple = [1, 0, 1, 1]   # Фиолетовый

class VBoxLayoutExample(App):
    def build(self):
        # Создаем вертикальный layout с отступами:
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
