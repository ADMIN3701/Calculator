from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window
Window.size = (300, 500)

class MyApp(App):
    def update_label(self):
        self.label.text = self.primer

    def add_number(self, instance):
        if self.primer == "0":
            self.primer = ""

        self.primer += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if str(instance.text.lower()) == "x":
            self.primer += "*"
        else:
            self.primer += str(instance.text)
        self.update_label()

    def result(self, instance):
        self.label.text = str(eval(self.label.text))
        self.primer = self.label.text

    def build(self):
        self.primer = "0"
        al = AnchorLayout()
        bl = BoxLayout(orientation="vertical", padding=25)
        gl = GridLayout(cols=4, spacing=4, size_hint=(1, .6))

        self.label = Label(text="0", font_size=40, size_hint=(1, .4))
        bl.add_widget(self.label)

        gl.add_widget(Button(text="7", on_press=self.add_number))
        gl.add_widget(Button(text="8", on_press=self.add_number))
        gl.add_widget(Button(text="9", on_press=self.add_number))
        gl.add_widget(Button(text="X", on_press=self.add_operation))

        gl.add_widget(Button(text="4", on_press=self.add_number))
        gl.add_widget(Button(text="5", on_press=self.add_number))
        gl.add_widget(Button(text="6", on_press=self.add_number))
        gl.add_widget(Button(text="-", on_press=self.add_operation))

        gl.add_widget(Button(text="1", on_press=self.add_number))
        gl.add_widget(Button(text="2", on_press=self.add_number))
        gl.add_widget(Button(text="3", on_press=self.add_number))
        gl.add_widget(Button(text="+", on_press=self.add_operation))

        gl.add_widget(Widget())
        gl.add_widget(Button(text="0", on_press=self.add_number))
        gl.add_widget(Button(text=",", on_press=self.add_number))
        gl.add_widget(Button(text="=", on_press=self.result))

        bl.add_widget(gl)
        al.add_widget(bl)

        return al

if __name__ == "__main__":
    MyApp().run()