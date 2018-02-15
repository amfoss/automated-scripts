import sys
import test
import csv
cs=open('1.csv','r')
message=[]
y1=[]
y2=[]
y3=[]
y4=[]
y=[]
y1.append(10*"-"+'FIRST YEARS'+10*"-")
y2.append(10*"-"+'SECOND YEARS'+10*"-")
y3.append(10*"-"+'THIRD YEARS'+10*"-")
y4.append(10*"-"+"FOURTH YEARS"+10*"-")
message=test.main()
with cs:
	wcs = csv.reader(cs)
   	for row in wcs:
		if( row[2].strip() not in message):
			print(row[2])
			if(row[3] == '1'):
				y1.append(row[0]+row[1])
			elif(row[3] == '2'):
				y2.append(row[0]+row[1])
			elif(row[3] == '3'):
				y3.append(row[0]+row[1])
			elif(row[3] == '4'):
				y4.append(row[0]+row[1])
	y.append(y1)
	y.append(y2)
	y.append(y3)
	y.append(y4)
	for item in y:
		for string in item:
			print(string)