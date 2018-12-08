#-*- coding: windows-1250 -*-
import codecs


file_name = "example_ad9.txt"

file = codecs.open(file_name, "r", "windows-1250")
text = file.read()

text = text.replace("nigdy", "prawie nigdy")
text = text.replace(" oraz ", " temp ")
text = text.replace("dlaczego", "czemu")
text = text.replace(" i ", " oraz ")
text = text.replace(" temp ", " i ")
print(text)