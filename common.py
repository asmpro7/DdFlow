# standard imports
from datetime import datetime
from datetime import timedelta

formats = ["%d/%m/%Y", "%d/%-m/%Y", "%d-%m-%Y", "%d-%-m-%Y", "%d %m %Y", "%d %-m %Y", "%d.%m.%Y"]
Week_Day={1:["Monday","Images/mon.png"],2:["Tuesday","Images/tue.png"],3:["Wednesday","Images/wed.png"],4:["Thursday","Images/thu.png"],5:["Friday","Images/fri.png"],6:["Saturday","Images/sat.png"],7:["Sunday","Images/sun.png"]}

query_actions = {
    "weekday": ["weekday", "wkd"],
    "range": ["range", "rng"],
    "unix_time": ["unixtime", "unx"],
}

class InvalidDateError(Exception):
    def __str__(self):
        return "Please enter a valid date (d/m/yyyy)"
    
class UnknownActionKeyword(Exception):
    def __init__(self, keyword):
        self.keyword = keyword

    def __str__(self):
        return "unkown action keyword '" + self.keyword + "'."
    
class StrToDate:
    """context manager to convert strings into datetime objects
    using pre-set date formats. Will raise InvalidDateError if
    one of the dates is not of a particular date.
    """
    def __init__(self, *datestrings):
        self.datestrings = datestrings
        print(self.datestrings)
    
    def __enter__(self):
        dates = []
        for datestr in self.datestrings:
            dt = None
            for format_str in formats:
                try:
                    dt = datetime.strptime(datestr, format_str)
                except ValueError:
                    continue
            if dt is None:
                raise InvalidDateError()
            
            dates.append(dt)
        return dates
    
    def __exit__(self, exc_type, exc_val, traceback):
        pass