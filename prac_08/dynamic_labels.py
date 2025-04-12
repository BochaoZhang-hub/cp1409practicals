from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label

class DynamicLabel(App):
    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root
    def on_start(self):
        self.generate_labels()

    def generate_labels(self):
        names = ["Alice", "Bob", "Cassi", "David", "Elon", "Fox"]

        labels_box = self.root.ids.main
        labels_box.clear_widgets()

        for name in names:
            label = Label(text=name)
            labels_box.add_widget(label)

DynamicLabel().run()

