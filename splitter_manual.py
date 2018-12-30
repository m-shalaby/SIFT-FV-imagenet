import csv
import numpy as np

def getSizesList(input_filenameY):
    sizes_list = [] 
    counter = 0
    classes_counter = 0
    with open(input_filenameY) as file:
        lines = [int(line.strip()) for line in file.readlines()]
        for i in range(len(lines)):
            if(classes_counter == lines[i]):
                counter += 1            
            else: # new class encountered
                sizes_list.append(counter)
                counter = 1 # reset counter
                classes_counter += 1
            if(i == len(lines) - 1):
                sizes_list.append(counter)
    return sizes_list
sizes_list = getSizesList('labels_copy.csv')
global_counter = 0
test = []
valid = []
train = []
for size in sizes_list:
    valid = valid + list(range(global_counter, global_counter+50))
    global_counter += 50
    test = test + list(range(global_counter, global_counter+150))
    global_counter += 150
    train = train + list(range(global_counter, global_counter+size-200))
    global_counter += size-200

with open('fisher_vectors_copy.csv', 'rt') as inp, open('train_split.csv', 'wt') as out_train, open('valid_split.csv', 'wt') as out_valid, open('test_split.csv', 'wt') as out_test:
    writer_train = csv.writer(out_train)
    writer_valid = csv.writer(out_valid)
    writer_test = csv.writer(out_test)
    i = 0
    for row in csv.reader(inp):
        if i in valid:
            writer_valid.writerow(row)
            print(i)
            i = i+1
        elif i in test:
            writer_test.writerow(row)
            print(i)
            i = i+1
        else:
            writer_train.writerow(row)
            print(i)
            i = i+1

with open('labels_copy.csv', 'rt') as inp, open('train_label_split.csv', 'wt') as out_train, open('valid_label_split.csv', 'wt') as out_valid, open('test_label_split.csv', 'wt') as out_test:
    writer_train = csv.writer(out_train)
    writer_valid = csv.writer(out_valid)
    writer_test = csv.writer(out_test)
    i = 0
    for row in csv.reader(inp):
        if i in valid:
            writer_valid.writerow(row)
            print(i)
            i = i+1
        elif i in test:
            writer_test.writerow(row)
            print(i)
            i = i+1
        else:
            writer_train.writerow(row)
            print(i)
            i = i+1