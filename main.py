from kivy.app import App
from kivy.uix import layout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image



Window.size = (360, 600)


class MainApp(App):
    def build(self):

        img = Image(source='IPS.jfif', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=50,
                            spacing=15, padding=20)
        self.measured = TextInput(hint_text='Enter measured here:')
        self.by_default = TextInput(hint_text='Enter by_default here:')
        submit = Button(text="Submit", on_press=self.submit)
        layout.add_widget(self.measured)
        layout.add_widget(self.by_default)
        layout.add_widget(submit)
        layout.add_widget(img)

        return layout

    def submit(self, obj):
        result = abs(float(self.measured.text) - float(self.by_default.text)) * 100 / float(self.by_default.text)
        self.res = TextInput(text=f"{result}")

        return result

    def show_data(self, obj):
        pass




MainApp().run()
