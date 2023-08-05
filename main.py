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
from common import *

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
                    with StrToDate(query_parts[1], query_parts[2]) as datetimes:
                        timedelta = datetimes[0] - datetimes[1]
                        output.append({
                            "Title": f"{abs(timedelta.days)} days",
                            "IcoPath": "images/app.png"
                        })

                elif query_parts[0] in query_actions["unix_time"]:
                    with StrToDate(query_parts[1]) as datetimes:
                        output.append({
                            "Title": f"{int(datetimes[0].timestamp())} in Unix time",
                            "IcoPath": "images/app.png"
                        })
                
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
                "Title": "",
                "IcoPath": "Images/error.png"})

        return output
    

if __name__ == "__main__":
    DdFlow()
