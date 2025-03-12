class ProgrammingLanguage:
    """
    estimated doing time : 1 hour
    actual doing time : 30 mins
    """
    def __init__(self, name, typing, reflection, year):
        """initializing all the statues of the program"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """check if the return is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """return str form"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
