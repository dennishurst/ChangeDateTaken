import datetime
from os.path import exists
import os

def Month_Name_Using_Date(date):
    Month_name=date.strftime('%b')
    return Month_name


sRoot = "E:\\PicturesWorking"

for year in range(1990, 2026):
    folder = f"{sRoot}\\{year}"
    if exists(folder):
        print (f"{folder} exists")
    else:    
        print (f"{folder} does not exists")
        os.makedirs(folder)
           

    for month in range(1,13):
        folder = f"{sRoot}\\{year}\\{month} {Month_Name_Using_Date(datetime.date(year,month,1))}"
        if exists(folder):
            print (f"{folder} exists")
            
        else:    
            print (f"{folder} does not exists")
            os.makedirs(folder)


