import numpy as np

input_filename_X = 'fisher_vectors_copy.csv'
input_filename_Y = 'labels_copy.csv'




# get sizes of each class in the dataset
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

# split dataset
def splitFV(input_filenameX, input_filenameY, valid_size = 50, test_size = 150, num_classes = 200, vect_length = 6400):        
    # get number of vectors for each class
    sizes_list = getSizesList(input_filenameY)
    
    # read input as memmap file
    input_X = np.memmap(input_filenameX, mode='r', shape=(sum(sizes_list),6400))

    # total numbers
    num_valid = valid_size * num_classes
    num_test = test_size * num_classes
    num_train = sum(sizes_list) - num_valid - num_test    
    
    # memmap files for valid, test and train
    valid_memmap = np.memmap("valid_set_X.csv", mode='w+', shape=(num_valid, vect_length))
    test_memmap = np.memmap("test_set_X.csv", mode='w+', shape=(num_test, vect_length))
    train_memmap = np.memmap("train_set_X.csv", mode='w+', shape=(num_train, vect_length))
    
    # index counters
    counter_global = 0
    counter_valid = 0
    counter_test = 0
    counter_train = 0
    
    for size in sizes_list: # size = class size
        train_size = size - valid_size - test_size
        
        # fill in validation set
        valid_memmap[counter_valid:counter_valid + valid_size] = input_X[counter_global:counter_global + valid_size]
        counter_valid += valid_size
        counter_global += valid_size
        
        # fill in test set
        test_memmap[counter_test:counter_test + test_size] = input_X[counter_global:counter_global + test_size]
        counter_test += test_size
        counter_global += test_size
        
        # fill in training set
        train_memmap[counter_train:counter_train + train_size] = input_X[counter_global:counter_global + train_size]
        counter_train += train_size
        counter_global += train_size

    return train_memmap, valid_memmap, test_memmap

def splitLabel(input_filenameY, valid_size = 50, test_size = 150, num_classes = 200):
    # get number of data for each class
    sizes_list = getSizesList(input_filenameY)

    # labels to write
    valid_file = open("valid_labels.csv", 'w')
    test_file = open("test_labels.csv", 'w')
    train_file = open("train_labels.csv", 'w')
    
    for i in range(num_classes):
        for j in range(sizes_list[i]):
            if j < valid_size:
                valid_file.write("%i\n"%(i))
            elif j < (valid_size+test_size):
                test_file.write("%i\n"%(i))
            else:
                train_file.write("%i\n"%(i))      
    
    valid_file.close()
    test_file.close()
    train_file.close()

    return train_file, valid_file, test_file


# splitFV(input_filename_X, input_filename_Y)
# splitLabel(input_filename_Y)
