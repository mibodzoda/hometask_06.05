def is_symbol(n):
    if n in "!@$%^&*±§":
        return True
    else:
        return False
    
a = input()

for i in a:
    if is_symbol(i):
        i = i.replace(i, '#')
print(i, end='')