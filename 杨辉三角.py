def triangles():
    num = 0
    while True:
        if num == 0:
            num += 1
            yield [1]
        elif num == 1:
            num += 1
            tmp = [1,1]
            yield [1,1] 
        else:
            length = tmp.__len__() + 1
            tmp = [1 if i == 0 or i == length - 1 else tmp[i] + tmp[i - 1] for i in range(length)]
            yield tmp


if __name__ == '__main__':
    n = 0
    results = []
    for t in triangles():
        print(t)
        n = n + 1
        if n == 10:
            break
