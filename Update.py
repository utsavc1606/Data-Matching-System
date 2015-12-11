'''
Created on Dec 9, 2015

@author: utsavchatterjee
'''
import csv
from itertools import count
filePath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/input_files/"
outputPath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/output_files/"
kbPath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/KnowledgeBase/"
cn = count(880000000)
progressCounter = 1

with open(filePath+"Licenses_RefID.csv") as inputFile, open(outputPath+"Licenses_RefID_IU.csv","w") as outputFile, open(kbPath+"KnowledgeBase.csv","r") as lookupFile:
    reader, writer, lookup = csv.reader(inputFile, delimiter="|"), csv.writer(outputFile, delimiter="|"), csv.reader(lookupFile, delimiter="|")
    head, lkpdict, d = next(reader), {}, {}
    writer.writerow(["ID"]+head)
    
    for row in lookup:
        lkpdict[row[5]] = row[0]
        
    for record in reader:
        progressCounter+=1
        print progressCounter
        v = record[4]
        if v in lkpdict.keys():
            writer.writerow([lkpdict[v]] + record)
        else:
                if v in d:
                    writer.writerow([d[v]]+record)
                else:
                    i = next(cn)
                    d[v] = i
                    writer.writerow([i]+record)
#                     print record
#                   

inputFile.close()
outputFile.close()
lookupFile.close()                    