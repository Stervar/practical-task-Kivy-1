import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class VBoxLayoutExample(App):
    # Color definitions
    red = [1, 0, 0, 1]      
    green = [0, 1, 0, 1]   
    blue = [0, 0, 1, 1]     
    purple = [1, 0, 1, 1]

    def build(self):
        # padding=[слева, сверху, справа, снизу]
        layout = BoxLayout(
            orientation='vertical',
            padding=[30, 50, 30, 20],  # Отступы: слева 30, сверху 50, справа 30, снизу 20
            spacing=20                  # Расстояние между кнопками
        )

        colors = [self.red, self.green, self.blue, self.purple]

        for i, color in enumerate(colors):
            btn = Button(
                text=f"Кнопка {i+1}",
                background_color=color,
                size_hint=(1, 0.2)  # Ширина 100%, высота 20% от layout
            )
           
            btn.bind(on_press=self.on_press_button)
            layout.add_widget(btn)

        return layout
 
    def on_press_button(self, instance):
        print('Вы нажали на кнопку!')


if __name__ == "__main__":
    VBoxLayoutExample().run()
