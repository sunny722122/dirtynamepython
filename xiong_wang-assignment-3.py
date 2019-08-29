import writelistinfile
import csv
import sys
import re

binvalid=None
#define characters which is valid
valid_expresion=re.compile(r'^[A-Za-z]+\-{0,1}[A-Za-z]*$')
#store those invalid names in the file
Invalidname=[]
#store raw clean names, which mixed upper and lower case
cleanrawname=[]
#store clean names, first letter in upper case, otherwise in lower case
cleanname=[]
#open dirtyname file
#check these file exist, if already exist, delete it
writelistinfile.dumpfile('InvalidNames.csv')
writelistinfile.dumpfile('RawCleanNames.csv')
writelistinfile.dumpfile('CleanNames.csv')

try:
        #read dirty names into list
        readCSV=writelistinfile.readfileintolst('10000000DirtyNames.csv')
        for row in readCSV:
            #read whole row into row
            for item in row:
                matchresult=valid_expresion.match(item)
                #print(item,matchresult)
                if str(matchresult)=="None":
                    Invalidname.append(item)
                elif item[len(item)-1]=='-':
                    Invalidname.append(item)
                else:
                    cleanrawname.append(item)
                if len(Invalidname)>100:
                    #write invalidname list into file
                    writelistinfile.Writelistintofile('InvalidNames.csv',Invalidname)
                    Invalidname.clear()
                if len(cleanrawname)>100:
                    writelistinfile.Writelistintofile('RawCleanNames.csv',cleanrawname)
                    cleanrawname.clear()
except:#if file not exist exit the program
    print("File with dirty names not found!")
    sys.exit("File not found program terminated!")



#change raw clean name into clean name, format it in first letter in uppercase
#second onwards in lower case
try:
        #read raw clean names into list
        readRawCSV=writelistinfile.readfileintolst('RawCleanNames.csv')
        for row in readRawCSV:
            #read whole row into row
            for item in row:
                newname=[]
                for i in range(len(item)):
                    #format the first letter into uppercase
                    if i==0:
                        newname.append(item[i].upper())
                    else:#format the rest letter into lowercase
                        newname.append(item[i].lower())
                
                #make the individual character into word
                strnewname=''.join(newname)
                #print(strnewname)
                #store the new word into clean name
                cleanname.append(strnewname)
                if len(cleanname)>100:
                    #write clean name list into file
                    writelistinfile.Writelistintofile('CleanNames.csv',cleanname)
                    cleanname.clear()
except:
    print("Error!")
    sys.exit("Program terminated!")

