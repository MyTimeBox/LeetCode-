{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def IsBinarySortTreeSequence(lst):\n",
    "    if not lst:\n",
    "        return False\n",
    "    \n",
    "    # 取根结点\n",
    "    root = lst[-1]\n",
    "    length = lst.__len__()\n",
    "    \n",
    "    # 根结点前面的序列可以分为两部分，左边节点值都小于根结点，右边节点值都大于根结点\n",
    "    index = 0\n",
    "    # 找到两组数据的分界点的index\n",
    "    while index < length - 1:\n",
    "        tmp = lst[index]\n",
    "        if tmp > root:\n",
    "            break\n",
    "        else:\n",
    "            index += 1\n",
    "    \n",
    "    # 判断右侧数据是否都大于root\n",
    "    mid = index\n",
    "    while mid < length - 1:\n",
    "        tmp = lst[mid]\n",
    "        if tmp <= root:\n",
    "            return False\n",
    "        else:\n",
    "            mid += 1\n",
    "    \n",
    "    # 如果左右两组数据都存在，则开始判断子节点\n",
    "    left, right = True, True\n",
    "    if index > 0:\n",
    "#         print('left',lst[0:index])\n",
    "        left = IsBinarySortTreeSequence(lst[0:index])\n",
    "    if index < length - 1:\n",
    "#         print('right', lst[index:-1])\n",
    "        right = IsBinarySortTreeSequence(lst[index:-1])\n",
    "    \n",
    "    return left and right\n",
    "\n",
    "\n",
    "l1 = [5,7,6,9,11,10,8]\n",
    "l2 = [7,4,6,5]\n",
    "l3 = []\n",
    "l4 = [1,2,3,4]\n",
    "print(IsBinarySortTreeSequence(l1))\n",
    "print(IsBinarySortTreeSequence(l2))\n",
    "print(IsBinarySortTreeSequence(l3))\n",
    "print(IsBinarySortTreeSequence(l4))        \n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
