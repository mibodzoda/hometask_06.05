list1 = input().split()

list2 = []
for i in list1:
    if not (i == "" or i == None):
        list2.append(i)
print(list2)