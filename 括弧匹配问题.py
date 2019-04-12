问题:

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例：
    示例 1:
    输入: "()"
    输出: true

    示例 2:
    输入: "()[]{}"
    输出: true
    
题解: 用栈存储左括弧，遍历字符串，遇到右括弧判断是否与栈顶元素匹配
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        else:
            # 用列表模拟栈，若是做括号则入栈，若是右括弧，则抛出栈顶元素，若跟右括弧匹配，则继续遍             # 历，否则返回False
            stack = []
            chars = {')': '(', '}': '{', ']': '['}
            is_valid = True
            for i in s:
                if i in chars.values():  # 左括弧入栈
                    stack.append(i)
                else:
                    if stack:
                        top = stack[len(stack) - 1]
                        if top == chars[i]:
                            # 匹配则删除栈顶元素
                            stack.pop()
                        else: # 括弧不匹配,无效
                            is_valid = False
                            break
                    else:  # 右括弧较多,无效
                        is_valid = False
                        break
            if stack:
                is_valid = False  # 左括弧较多,无效
            return is_valid
                    
                    
        
