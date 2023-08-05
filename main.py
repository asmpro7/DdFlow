# -*- coding: utf-8 -*-
# third party imports

# standard imports
import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))
from datetime import datetime
from datetime import timedelta

# local imports
from flowlauncher import FlowLauncher
from exceptions import *

formats = ["%d/%m/%Y", "%d/%-m/%Y", "%d-%m-%Y", "%d-%-m-%Y", "%d %m %Y", "%d %-m %Y", "%d.%m.%Y"]
Week_Day={1:["Monday","Images/mon.png"],2:["Tuesday","Images/tue.png"],3:["Wednesday","Images/wed.png"],4:["Thursday","Images/thu.png"],5:["Friday","Images/fri.png"],6:["Saturday","Images/sat.png"],7:["Sunday","Images/sun.png"]}

query_actions = {
    "weekday": ["weekday", "wkd"],
    "range": ["range", "rng"],
    "unix_time": ["unixtime", "unx"],
}

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

class DdFlow(FlowLauncher):

    def query(self, query):
        output=[]

        try:
             
            if len(query.strip()) == 0:
                output.append({
                    "Title": "DdFlow",
                    "SubTitle": "Enter a DdFlow action keyword (e.g., range, weekday, unix time etc...)",
                    "IcoPath": "Images/app.png"})
            else:
                query_parts = query.lower().split()

                if query_parts[0] in query_actions["weekday"]:
                    with StrToDate(query_parts[1]) as datetimes:
                        output.append({
                        "Title": f"{Week_Day[datetimes[0].isoweekday()][0]}",
                        "IcoPath": f"{Week_Day[datetimes[0].isoweekday()][1]}"})

                elif query_parts[0] in query_actions["range"]:
                    raise Exception

                elif query_parts[0] in query_actions["unix_time"]:
                    # TODO: implement unix time conversion functionality
                    raise Exception
                
                else:
                    raise UnknownActionKeyword(query_parts[0])
                
        except InvalidDateError as ex:
            output.append({
                "Title": str(ex),
                "IcoPath": "Images/error.png"})
        except UnknownActionKeyword as ex:
            output.append({
                "Title": str(ex),
                "IcoPath": "Images/error.png"})
        except Exception as ex:
            print(ex)
            output.append({
                "Title": "an unknown error had occured",
                "IcoPath": "Images/error.png"})
                         

        return output
    

if __name__ == "__main__":
    DdFlow()
