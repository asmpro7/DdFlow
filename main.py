# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
from datetime import datetime
formats = ["%d/%m/%Y", "%d/%-m/%Y", "%d-%m-%Y", "%d-%-m-%Y", "%d %m %Y", "%d %-m %Y"]
Week_Day={1:["Monday","Images/mon.png"],2:["Tuesday","Images/tue.png"],3:["Wednesday","Images/wed.png"],4:["Thursday","Images/thu.png"],5:["Friday","Images/fri.png"],6:["Saturday","Images/sat.png"],7:["Sunday","Images/sun.png"]}

class DdFlow(FlowLauncher):

    def query(self, query):
        output=[]
        try:
             
            if len(query.strip()) == 0:
                    output.append({
                        "Title": "Enter Date (d/m/yyyy)",
                        "SubTitle": "you can ues leading zeros and spaces",
                        "IcoPath": "Images/app.png"})
            else:
                 for format_str in formats:
                        dt = datetime.strptime(query, format_str)
                        output.append({
                        "Title": f"{Week_Day[dt.isoweekday()][0]}",
                        "IcoPath": f"{Week_Day[dt.isoweekday()][1]}"})
                        break
        except:
             output.append({
                        "Title": "enter a valid date",
                        "IcoPath": "Images/error.png"})
                         

        return output
if __name__ == "__main__":
    DdFlow()
