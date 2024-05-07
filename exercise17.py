a = input()
str1 = a.split()
res = []
for i in str1:
    if any(char.isalpha() for char in i) and any(char.isdigit() for char in i):
        res.append(i)
for j in res:
    print(j)