class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Stack is intialised to be empty #
        mapping = {')':'(', '}':'{', ']':'['} # This dictionary provides us with closing brackets with respective opening brackets #
        for char in s:
            if char in mapping:
                if stack: # Stack is not empty #
                    top_element = stack.pop()
                else:
                    top_element = '#'
                if mapping[char] != top_element: # Comparing popped bracket with matching opening bracket #
                    return False # If not match #
            else:
                stack.append(char) # Adding opening bracket for later closing bracket #
        return not stack # If stack is empty, it means all executed so true
