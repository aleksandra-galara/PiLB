import os

path = "/home"

for path, subdirs, files in os.walk(path):
	for file in files:
		if os.path.isfile(os.path.join(path,file)):
			print (file)