def is_digit(n):
    try:
        int(n)
        return True
    except:
        return False

a = input()
for i in a:
    if is_digit(i):
      print(i, end='')