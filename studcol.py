import csv
filename=input("enter the csv file name(with.csv extension):")
colread=input("enter column indices to read(comma-separated,starting from 0):")
colread=[int(x.strip())for x in colread.split(",")]
with open(filename,'r')as csvfile1:
    csvreader=csv.reader(csvfile1)
    for row in csvreader:
        selectcol=[row[col]for col in colread if col<len(row)]
        print(selectcol) 
