from PIL import Image

file_names = ["lena1.jpg","lena2.jpg","lena3.jpg","lena4.jpg"]

for file in file_names:
	im = Image.open(file)
	im.save(file[:-4] + ".png")