class InvalidDateError(Exception):
    def __str__(self):
        return "Please enter a valid date (d/m/yyyy)"
    
class UnknownActionKeyword(Exception):
    def __init__(self, keyword):
        self.keyword = keyword

    def __str__(self):
        return "unkown action keyword '" + self.keyword + "'."