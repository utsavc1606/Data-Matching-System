'''
Created on Dec 9, 2015

@author: utsavchatterjee
'''
filePath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/input_files/"
inputFile = filePath+"Licenses_Cleaned.csv"
outputFile = filePath+"Licenses_RefID.csv"
prefix = "lic_" 
inputReader = open(inputFile,'r')
outputWriter = open(outputFile, 'w')
counter = 1
header = inputReader.readline()
outputWriter.write("RefID|"+header)
for lines in inputReader:
    outputWriter.write(prefix+str(counter)+"|"+lines)
    counter+=1
    
outputWriter.close()
inputReader.close()    