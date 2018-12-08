#-*- coding: windows-1250 -*-
import codecs


file_name = "example_ad9.txt"

file = codecs.open(file_name, "r", "windows-1250")
text = file.read()

text = text.replace("nigdy", "")
text = text.replace(" się ", " ")
text = text.replace(" oraz ", " ")
text = text.replace("dlaczego", "")
text = text.replace(" i ", " ")
print(text)