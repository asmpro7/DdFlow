class InvalidDateError(Exception):
    def __str__(self):
        return "Please enter a valid date (d/m/yyyy)"