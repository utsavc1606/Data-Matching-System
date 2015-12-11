'''
Created on Dec 9, 2015

@author: utsavchatterjee

Capture
'''  
import csv
from itertools import count
cn = count(1001)
filePath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/input_files/"
outputPath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/output_files/"
kbPath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/KnowledgeBase/"

with open(filePath+"BaseSalary_RefID.csv") as f, open(outputPath+"BaseSalary_IC.csv","w") as tmp:
    r, wr = csv.reader(f, delimiter="|"), csv.writer(tmp, delimiter="|")
    head, d = next(r), {}
    wr.writerow(["ID"]+head)
    for row in r:
        v = row[4]
        if v in d:
            wr.writerow([d[v]] + row)
        else:
            i = next(cn)
            d[v] = i
            wr.writerow([i] + row)

f.close()
tmp.close()

