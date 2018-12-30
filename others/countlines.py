#the purpose of this is to count the number of lines in the massive visual bag of words csv files to allow the creation of memory mapped files

import csv

with open('/Users/m_ayman/Desktop/Life/Courses/Fall 2018/Comp551/Final Project/ALLDATAcomp/vbow_train.csv', 'r') as f:
	str_data = f.readlines()
	print(len(str_data))

with open('/Users/m_ayman/Desktop/Life/Courses/Fall 2018/Comp551/Final Project/ALLDATAcomp/vbow_test.csv', 'r') as f:
	str_data = f.readlines()
	print(len(str_data))

with open('/Users/m_ayman/Desktop/Life/Courses/Fall 2018/Comp551/Final Project/ALLDATAcomp/vbow_valid.csv', 'r') as f:
	str_data = f.readlines()
	print(len(str_data))
