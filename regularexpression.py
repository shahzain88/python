import re

pattern = re.compile("for me buggy i said youtube")

string = "for me buggy i said youtube"

a = pattern.search(string)
print(a)
print(a.span())
print(a.start())
print(a.end())
print(a.group())
b = pattern.findall(string)
print(b)
c = pattern.fullmatch(string)
print(c)
d = pattern.match(string)
print(d)
