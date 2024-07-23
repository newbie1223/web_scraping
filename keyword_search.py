import csv

keyword1 = 'コク'
keyword2 = 'ある'

l = []
i=0
with open('./reviews/reviews_asahi-super-dry.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for x in row:
            if keyword1 in x:
                if keyword2 in x:
                    l.append(x)
                    i+=1
print(l)
print(i)