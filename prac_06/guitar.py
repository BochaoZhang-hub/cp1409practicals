class Guitar:
    """This is the class for the guitar"""
    """estimated time : 15 mins """
    """actual time : 10 mins """
    def __init__(self, name="", year=0, cost=0):
        """this function will initialize the guitar and give its name year and cost
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """this function will return the str type of the guitars properties."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year=2025):
        """This represents the year of the guitar's existence."""
        return current_year - self.year

    def is_vintage(self):
        """This function will judge if the guitar is older than 50 years old. """
        return self.get_age() >= 50
