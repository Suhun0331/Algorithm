while True:
    try:
        lst = list(input())
        big = 0
        small = 0
        blank = 0
        num = 0
        for i in lst:
            if ord('a')<=ord(i)<=ord('z'):
                small +=1
            elif ord('A')<=ord(i)<=ord('Z'):
                big += 1
            elif i == ' ':
                blank += 1
            elif i.isdigit():
                num += 1
        print("{} {} {} {}".format(small, big, num, blank))
    except EOFError:
        break