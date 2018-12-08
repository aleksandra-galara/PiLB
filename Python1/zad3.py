import os

path = '/home/witcherek7'
file_list = os.listdir(path)
number_of_files = 0

for file in file_list:
	if os.path.isfile(os.path.join(path,file)):
		number_of_files = number_of_files + 1

print(number_of_files)
