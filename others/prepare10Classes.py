#extracting only 10 classes for some very preliminary testing of our methodology

import csv
with open('fisher_vectors_10classes.csv', 'rt') as inp, open('training_prel.csv', 'wt') as out, open('valid_prel.csv', 'wt') as out2:
    writer = csv.writer(out)
    writer2 = csv.writer(out2)
    i = 1
    for row in csv.reader(inp):
        if (i>50 and i<1500) or (i>1550 and i<2800) or (i>2850 and i<4000) or (i>4050 and i<5500) or (i>5550 and i<7000) or (i>7050 and i<8600) or (i>8650 and i<10000) or (i>10050 and i<11000) or (i>11050 and i<12500) or (i>12550 and i<13250) or (i>13300):
            writer.writerow(row)
            print(i)
            i = i+1
        else:
            writer2.writerow(row)
            print(i)
            i = i+1

with open('labels_10classes.csv', 'rt') as inp, open('train_labels_prel.csv', 'wt') as out, open('valid_labels_prel.csv', 'wt') as out2:
    writer = csv.writer(out)
    writer2 = csv.writer(out2)
    i = 1
    for row in csv.reader(inp):
        if (i>50 and i<1500) or (i>1550 and i<2800) or (i>2850 and i<4000) or (i>4050 and i<5500) or (i>5550 and i<7000) or (i>7050 and i<8600) or (i>8650 and i<10000) or (i>10050 and i<11000) or (i>11050 and i<12500) or (i>12550 and i<13250) or (i>13300):
            writer.writerow(row)
            print(i)
            i = i+1
        else:
            writer2.writerow(row)
            print(i)
            i = i+1
