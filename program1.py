class Solution(object):
    def isValid(self, s):
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map.values():  
                stack.append(char)
            elif char in bracket_map.keys():  
                if not stack or stack.pop() != bracket_map[char]:
                    return False
    
        return len(stack) == 0 
        """
        :type s: str
        :rtype: bool
        """
        pass







    



  

