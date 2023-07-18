# -*- coding: utf-8 -*-
# third party imports

# standard imports
import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))
from datetime import datetime

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

class DdFlow(FlowLauncher):

    def query(self, query):
        output=[]

        query = "wkd 05.01.2023"
        try:
             
            if len(query.strip()) == 0:
                output.append({
                    "Title": "DdFlow",
                    "SubTitle": "Enter a DdFlow action keyword (e.g., range, weekday, unix time etc...)",
                    "IcoPath": "Images/app.png"})
            else:
                query_parts = query.split()
                query_parts = list(map(lambda x: x.lower(), query_parts))

                if query_parts[0] in query_actions["weekday"]:
                    dt = None
                    for format_str in formats:
                        try:
                            dt = datetime.strptime(query_parts[1], format_str)
                        except ValueError:
                            continue
                        output.append({
                        "Title": f"{Week_Day[dt.isoweekday()][0]}",
                        "IcoPath": f"{Week_Day[dt.isoweekday()][1]}"})
                        break

                    if dt is None:
                        raise InvalidDateError()

                elif query_parts[0] in query_actions["range"]:
                    # TODO: implement range functionality
                    raise Exception

                elif query_parts[0] in query_actions["unix_time"]:
                    # TODO: implement unix time conversion functionality
                    raise Exception
                
        except InvalidDateError as ex:
            output.append({
                "Title": str(ex),
                "IcoPath": "Images/error.png"})
        except Exception:
            output.append({
                "Title": "an unknown error had occured",
                "IcoPath": "Images/error.png"})
                         

        return output
    

if __name__ == "__main__":
    DdFlow()
