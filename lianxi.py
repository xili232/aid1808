import re

f = open('1111.txt','rt')

data = f.read()

pattern = r'\b[A-Z]\S*\b'
pattern1 = r'-?\d+\.?/?\d*%?'
# it = re.findall(pattern,data)
it1 = re.findall(pattern1,data)
# print(it)
print(it1)
f.close()