from datetime import date

class ExpiredProductException(ValueError):

    def __init__(self, date_value: date):
        self.date_value = date_value
        self.today = date.today()
    
    def __str__(self):
        return f"Product expiration date: {self.date_value} is before today {self.today}"