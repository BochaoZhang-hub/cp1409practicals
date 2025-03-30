from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    calculated_result = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_mile_km_file.kv')
        return self.root

    def calculate_mile_to_km(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            result = miles * MILES_TO_KM
            self.calculated_result = f"{result:.2f} kilometers"
        except ValueError:
            self.calculated_result = "invalid input"

    def handle_increment(self, change):
        value = float(self.root.ids.input_miles.text) + change
        self.root.ids.input_miles.text = str(value)
        self.calculate_mile_to_km()

    def validate_numbers(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
