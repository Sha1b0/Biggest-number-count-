import re
fhand=open("Mboxx")
list1=list()
for line in fhand:
    line=line.rstrip()
    stuff=re.findall("^X-DSPAM-Confidence: ([0-9.]+)",line)
    if len(stuff) !=1: continue
    num=float(stuff[0])
    list1.append(num)
print('Maximum:',max(list1))
