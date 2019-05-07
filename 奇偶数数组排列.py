# 给出一个数组，将其中所有的奇数排在偶数前面

def solution(lst):
    front, back = 0, lst.__len__() - 1
    while front < back:
        front_num = lst[front]
        back_num = lst[back]
        front_yu = front_num % 2
        back_yu = back_num % 2
        if front_yu == 0 and back_yu == 1:
            lst[front], lst[back] = back_num, front_num
            front += 1
            back -= 1
        elif front_yu == 1:
            front += 1
        elif back_yu == 0:
            back -= 1
    print(lst)
    
    

solution([1,2,3,4])
solution([4,3,2,1])
solution([1])
