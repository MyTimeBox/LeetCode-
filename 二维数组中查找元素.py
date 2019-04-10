#题目:在一个二维数组中，每一行都按照从左到右递增的顺序排列，每一列按从上到下的顺序排列，给定一个二维数组matrix和一个数num，判断这个数是否在二维数组中

#   二维数组示例:   
#   1  2  8  9
#   2  4  9  12
#   4  7  19  13
#   6  8  11  15

#解析:   先选取最右上角的数m与给定的数num比较，若 m > num，则 num 肯定不在 m 所在的列中，将此列排除，继续查找；若 m < num, 则 num 肯定不在 m 所在   #        的行中，排除此行，继续查找
   
   
       
def Find_num_in_matrix(martix, rows, cols, num):
    if matrix:
        if rows > 0 and cols > 0:
            if num:
                row = 0
                col = cols - 1
                tmp = 0
                while row < rows and col >= 0:
                    tmp = matrix[row * cols + col]
                    if tmp == num:
                        return True
                    elif tmp > num:
                        col -= 1
                    else:
                        row += 1
                return False   # 如果 matrix 中没找到 num 则返回 Flase
            else:
                print('请输入要查找的数')
        else:
            print('请输入正确的行或列（正整数）')
    else:
        print('二维数组为空')
        return False
        

