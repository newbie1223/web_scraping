import csv

keyword = '甘み'

l = []
i=0
with open('./reviews/reviews_clear-asahi.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for x in row:
            if keyword in x:
                l.append(x)
                i+=1
print(l)
print(i)