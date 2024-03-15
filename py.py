from kivy.uix.textinput import TextInput
from kivy.app import App

class MyTextInputApp(App):
    def build(self):
        text_input = TextInput()
        text_input.bind(on_double_tap=self.on_double_tap)
        return text_input

    def on_double_tap(self, instance):
        # Custom behavior for double tap
        print("Double tap detected!")

if __name__ == '__main__':
    MyTextInputApp().run()
