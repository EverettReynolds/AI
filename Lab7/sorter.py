#!/usr/bin/python3

import math
import sys
import os











fl = ""
fileStr = ""
revStr = ""
lowerStr = ""
tokenStr = ""
listFiles = []
reviews = []
posrevs = []
wordlist = []
finalList = []
badwords = ["this", "that", "take", "want", "which", "then", "than", "will", "with", "have", "after", "such", "when", "some", "them", "could", "make", "though", "from", "were", "also", "into", "they", "their", "there", "because"]

path = r"/home/reynolds/CSC380/Lab7/reviews"
for files in os.listdir(path): 
    if os.path.isfile(os.path.join(path,files)):
        listFiles.append(files)
for files in listFiles:
    fl = files
    start = fl.find("_")
    end = fl.find(".")
    newfl = int(fl[start+1:end])
    if newfl > 5:
        posrevs.append(files)
#print(posrevs)
for files in posrevs:
    file1 = open('/home/reynolds/CSC380/Lab7/reviews/' + files,"r")  
    fileStr = fileStr + file1.read()
for char in fileStr:
    if char.isalnum() or char == ' ':
        revStr = revStr + char
lowerStr = str(revStr.lower())
#print(lowerStr)


for x in lowerStr:
    for y in badwords:
        if x == y:
            lowerStr.remove(x)

print(lowerStr)




