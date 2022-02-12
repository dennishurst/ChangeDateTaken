from datetime import datetime
import datetime
import piexif
import sys
import os

def ChangeDateTaken(filename, new_date):
    a = 1/0
    exif_dict = piexif.load(filename)
    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
    exif_bytes = piexif.dump(exif_dict)

    piexif.insert(exif_bytes, filename)

def Month_Name_Using_Date(date):
    Month_name=date.strftime('%b')
    return Month_name

def processDirectory(cwd, year, current_month, iFileCount):
    #
    # current_month can be
    #   1-12 representing actual months
    #    0 processing the root folder
    #   -1 representing a directory not in a month folder so we would use July 1st if setting a file
    #      but only if the date is not in the correct year or null

    
    print(f"processDirectory cwd: {cwd}, year: {year}, current_month: {current_month}, FileCount: {iFileCount}")

    monthsConsidered = {}
    if current_month == 0:
        #Need to process 12 sub folders for files
        for month in range(1,13):
            #print(f"{year} / {month} / 1")
            monthToConsider = datetime.date(year, month,1)
            
            monthFolder = f"{cwd}\\{month} {Month_Name_Using_Date(monthToConsider)}"
            #print(monthFolder)
            processDirectory(monthFolder, year, month, iFileCount)
            monthsConsidered[f"{month} {Month_Name_Using_Date(monthToConsider)}"] = monthFolder

    
    #Now process all the folders, skipping already considered ones
    for dirs in os.listdir(cwd):
        if os.path.isfile(os.path.join(cwd, dirs)):
            #Dealing with files in a directory below
            pass

        else:
            try:
                alreadyDone = monthsConsidered[dirs] 
            except: 
                monSubDirectory = os.path.join(cwd, dirs)
                #print(f"monSubDirectory: {monSubDirectory}")
                if current_month == 0:
                    processDirectory(monSubDirectory, year, current_month, iFileCount)
                else:
                    processDirectory(monSubDirectory, year, current_month, iFileCount)
            

    for file in os.listdir(cwd):
        iFileCount['count'] = iFileCount['count'] + 1
        if os.path.isfile(os.path.join(cwd, file)):
            ext =  file.split('.')
            if ext[len(ext)-1].lower() == 'jpg':
                fullFile = os.path.join(cwd, file)
                #print(f"JPG File: {fullFile}")
            else:
                #print(f"Ignore File: {file} {ext[len(ext)-1].lower()}")
                pass
        else:
            #Dealing with dirs above
            pass



    #new_date = datetime(year, 7, 1, 0, 0, 0).strftime("%Y:%m:%d %H:%M:%S")

iFileCount = {"count": 0}

rootDir = os.getcwd()

rootDir = 'E:\\PicturesWorking\\2009'

print(f"Processing: {rootDir}")

yearString = rootDir.split('\\')


year = int(yearString[len(yearString)-1])

if year < 1900:
    print(f"{year} is not a valid year")
    sys.exit(1)



processDirectory(rootDir, year, 0, iFileCount)

print(f'{iFileCount["count"]} files considered.')

sys.exit(0)


print(str(sys.argv))
a = input('press something')


