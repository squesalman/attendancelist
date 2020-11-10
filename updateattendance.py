# IMPORTANT : Transform the attendancelist extracted from MS Teams to UTF-8 code first!!
# Pandas script to read multiple csv file and remove duplicate from MS Teams attendance list
# Place the script in the same folder as your attendancelist csv
# Change the path accordingly in first cell and in to_csv function
# optional function dataframe.shape : to see how many rows and columns
# Optional function dataframe.head(0) : to see the headers
import pandas as pd
import glob

path = r'C:\Users\mshafique.salman\OneDrive - PETRONAS\Documents\Python\Attendance'
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename,index_col=None,header=0)
    li.append(df)

frame = pd.concat(li,axis=0,ignore_index=True)
newframe = frame.drop_duplicates(subset='Full Name',inplace=False)
newframe.to_csv(r'C:\Users\mshafique.salman\OneDrive - PETRONAS\Documents\Python\Attendance\attendancelist.csv',index=False)