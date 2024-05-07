def is_letter(n):
    if n in "abcdefghijklmnopqrstuvwxyz":
        return True
    else:
        return False
    
a = input()


for i in a:
    if is_letter(i):
        print(i, end="")