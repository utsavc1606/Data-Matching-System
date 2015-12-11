'''
Created on Dec 11, 2015

@author: utsavchatterjee
'''
inputPath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/input_files/join_files/"
outputPath = "/Users/utsavchatterjee/Documents/Python Projects/ERERescue/data/input_files/join_files/"

filenames = [inputPath+'Part1.csv', inputPath+'Part2.csv', inputPath+'Part3.csv', inputPath+'Part4.csv', inputPath+'Part5.csv', inputPath+'Part6.csv']
with open(outputPath+"joinedFile.csv", 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)