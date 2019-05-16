def IsBinarySortTreeSequence(lst):,
    if not lst:",
        return False",

    # 取根结点\n",
    root = lst[-1]
    length = lst.__len__()

    # 根结点前面的序列可以分为两部分，左边节点值都小于根结点，右边节点值都大于根结点\n",
    index = 0
    # 找到两组数据的分界点的index\n",
    while index < length - 1:
        tmp = lst[index
        if tmp > root:
            break
        else:
            index += 1

    # 判断右侧数据是否都大于root\n
    mid = index
    while mid < length - 1:
        tmp = lst[mid]
        if tmp <= root:
            return False
        else:
            mid += 1

    # 如果左右两组数据都存在，则开始判断子节点\n
    left, right = True, True
    if index > 0:
#         print('left',lst[0:index])\n
        left = IsBinarySortTreeSequence(lst[0:index])
    if index < length - 1:
#         print('right', lst[index:-1])\n
        right = IsBinarySortTreeSequence(lst[index:-1])

    return left and right
