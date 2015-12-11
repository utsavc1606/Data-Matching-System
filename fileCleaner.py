'''
Created on Dec 9, 2015

@author: utsavchatterjee
'''
filePath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/input_files/"
fileName = filePath+"Licenses.csv"
opFileName = filePath+'Licenses_Cleaned.csv'
dataFile = open(fileName, 'r')
outputFile = open(opFileName, 'w')
for lines in dataFile.readlines():
    try:
        if not lines.isspace():
            outputFile.write(lines)
        
    except:
        pass

outputFile.close()
dataFile.close()
