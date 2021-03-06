#给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

#给出数字到字母的映射与电话按键相同。注意 1 不对应任何字母。

#示例:
#    输入："23"
#    输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    
#题解：本题有很多解决思路，深度优先和广度优先是比较常用的两种方法。
#深度优先算法代码如下（）：

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dic = {
            "2": "abc","3": "def","4": "ghi","5": "jkl",
            "6": "mno","7": "pqrs","8": "tuv","9": "wxyz"
        }
        len_s = len(digits)
        
        def dfs(n, s):
            if n == len_s:
                res.append(s)
                return
            for ch in dic[digits[n]]:
                dfs(n+1, s+ch)
        if len_s == 0:
            return []
        dfs(0, '')
        return res
 
 
 #上述方法是参考的别人的解法，以下是我自己的解法：

    def letterCombinations(self, digits: str) -> List[str]:
        """广度优先，变体"""
        map_c = {
            '2':'abc','3':'def','4':'ghi','5':'jkl',
            '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'
        }
        
        def generate_lst(lv, lst):
            """
                输入：两个列表
                输出：这两个列表中元素两两组合的所有结果
            """
            res = []
            for i in lv:
                for j in lst:
                    res.append(i + j)
            return res
        
        
        loop_max = digits.__len__()
        res = []
        
        if loop_max == 1:
            res = list(map_c[digits[0]])
            
        elif loop_max > 1:
            res = list(map_c[digits[0]])
            for i in range(loop_max - 1):  
                res = generate_lst(res, map_c[digits[i + 1]]) 

        return res
    
    
