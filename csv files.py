import csv 
f = open('emp.csv') 
csv_reader = csv.reader(f) 
for rec in csv_reader: 
    print(rec) 
f.close() 