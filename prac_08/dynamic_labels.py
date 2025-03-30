from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

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
            label = Button(text=name)  # 用 Button 显示名字，因为你没学 Label
            labels_box.add_widget(label)

DynamicLabel().run()

