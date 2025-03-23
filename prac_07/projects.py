import datetime


class Project:
    """this is the project class"""

    def __init__(self, name, start_time, priority, cost, percentage_of_complete):
        """THis function will initialize the class"""
        self.name = name
        self.start_date = datetime.strptime(start_time, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost)
        self.percentage = int(percentage_of_complete)

    def __str__(self):
        """this function will return as a str type. """
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.percentage}%")

    def is_complete(self):
        """This function will test if its complete"""
        return self.percentage >= 100

    def __lt__(self, other):
        """This function will sort"""
        return self.priority < other.priority
