import os
import csv
file = open('data.txt', 'r')
cs=open('1.csv','w')
a=[]
original_email_ids=[]
with cs:
	write=csv.writer(cs)
	for line in file:
	    a=line.strip('|').split('|')
	    for item in a:
	        item.strip()		
	    write.writerow(a)    	    