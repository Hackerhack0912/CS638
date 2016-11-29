import sys
import pandas as pd
import numpy as np

# python split.py <inputFileName> <split_set_name1> <spli_set1_number> <split_set_name2> <split_set2_number>
input_file_name = sys.argv[1]
input_data = open(input_file_name)

split_set_1_file_name = sys.argv[2] + ".csv"
split_set_1_num = int(sys.argv[3])
split_set_1_file = open(split_set_1_file_name, "w")

split_set_2_file_name = sys.argv[4] + ".csv"
split_set_2_num = int(sys.argv[5])
split_set_2_file = open(split_set_2_file_name, "w")

data_points = []
line_count = 0
for line in input_data:
	if not line:
		continue
	else:
		if(line_count == 0):
			line_count += 1
			continue
		data_points.append(line)
		line_count += 1

total_data_num = line_count - 1

if(total_data_num != (split_set_1_num + split_set_2_num)):
	print("Non-consistent number")
	print("total_data_num: " + str(total_data_num))
	print("split_set_1_num: " + str(split_set_1_num))
	print("split_set_2_num: " + str(split_set_2_num)) 
	sys.exit(0)

set_1_index = np.random.choice(total_data_num, split_set_1_num, replace=False)

set_2_index = []

for index in range(total_data_num):
	if index not in set_1_index:
		set_2_index.append(index)


# write split dataset to the file
for index in set_1_index:
	split_set_1_file.write(data_points[index])

for index  in set_2_index:
	split_set_2_file.write(data_points[index])

split_set_1_file.close()
split_set_2_file.close()

