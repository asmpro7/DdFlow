# standard imports
from datetime import datetime
from datetime import timedelta

formats = ["%d/%m/%Y", "%d/%-m/%Y", "%d-%m-%Y", "%d-%-m-%Y", "%d %m %Y", "%d %-m %Y", "%d.%m.%Y"]
Week_Day={1:["Monday","Images/mon.png"],2:["Tuesday","Images/tue.png"],3:["Wednesday","Images/wed.png"],4:["Thursday","Images/thu.png"],5:["Friday","Images/fri.png"],6:["Saturday","Images/sat.png"],7:["Sunday","Images/sun.png"]}

query_actions = {
    "weekday": ["weekday", "wkd"],
    "range": ["range", "rng"],
    "unix_time": ["unixtime", "unx", "unix"],
}

class InvalidDateError(Exception):
    def __str__(self):
        return "Please enter a valid date (d/m/yyyy)"
    
class UnknownActionKeyword(Exception):
    def __init__(self, keyword):
        self.keyword = keyword

    def __str__(self):
        return "unkown action keyword '" + self.keyword + "'."

def str2date(*datestrings):
    dates = []
    for datestr in datestrings:
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