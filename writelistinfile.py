import sys
import os
import csv
#write listname content into file named filename
def Writelistintofile(filename,listname):
    try:
        with open(filename,'a') as writefile:
            for item in listname:
                writefile.write(item)
                writefile.write(',')
    except:
        print("File ",filename,"Writing fail!")
        sys.exit("Program terminated!")
#check if file exist, if exist then delete it
def dumpfile(filename):
    try:
        if os.path.isfile(filename):
            os.remove(filename)
        else:
            pass
    except:
        print("File ",filename,"Dump fail!")
        sys.exit("Program terminated!")
        
#read file into list
def readfileintolst(filename):
    rtlist=[]
    try:
        with open(filename) as csvfile:
            #seperate items by ','
            readRawCSV=csv.reader(csvfile, delimiter=',',quotechar='|')
            rtlist=list(readRawCSV)   
        return rtlist
    except:
        print("File ",filename," open fail!")
        sys.exit("Program terminated!")
