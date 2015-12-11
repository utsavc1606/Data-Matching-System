'''
Created on Dec 10, 2015

@author: utsavchatterjee
'''
import csv
import hashlib

inputPath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/KnowledgeBase/"
outputPath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/output_files/final_outputs/"
inputFile = "KnowledgeBase.csv"
outputFile = inputFile+"_final.csv"

with open(inputPath+inputFile) as f, open(outputPath+outputFile,"w") as op:
    r, w = csv.reader(f, delimiter = "|"), csv.writer(op, delimiter = "|")
    head = next(r)
    
    for line in r:
        assigned_id = line[0]
        rid = [str(hashlib.md5(assigned_id).hexdigest())[:12].upper()]
        groups = str(line).split("|")
        n = 7
#         w.writerow(rid + [str('|'.join(groups[n:]))])
        w.writerow(rid+ [line[1]]+[line[2]]+[line[3]]+[line[4]]+[line[5]]+[line[6]])
#+[line[13]]+[line[14]]+[line[15]]+[line[16]]+[line[17]]+[line[18]]+[line[19]]+[line[20]]+[line[21]]+[line[22]])

    
    