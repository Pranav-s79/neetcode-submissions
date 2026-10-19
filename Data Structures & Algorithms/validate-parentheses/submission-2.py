class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_map = {')':'(', '}': '{', ']': '['}
        for string in s:
            if string in dict_map:
                if stack and stack[-1] == dict_map[string]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(string)
        
        return True if not stack else  False
