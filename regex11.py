import re 

pattern = r'(\w+):(\d+)'

s = 'zhang:1994 li:1993'

l = re.findall(pattern,s)
print(l)