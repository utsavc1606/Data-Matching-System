'''
Created on Dec 9, 2015

@author: utsavchatterjee
'''
import csv
outputPath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/output_files/"
kbPath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/KnowledgeBase/"

with open(outputPath+"Licenses_RefID_IU.csv", "r") as icFile, open(kbPath+"KnowledgeBase.csv", "a") as kb:
    reader, kbwr = csv.reader(icFile, delimiter="|"), csv.writer(kb, delimiter="|")
    for rows in reader:
#         print rows[1]
        kb.write(rows[0]+"|"+rows[1]+"|"+rows[2]+"|"+rows[3]+"|"+rows[4]+"|"+rows[5]+"|"+rows[6]+"\n")
        
kb.close()         
