class Solution:
    def isValid(self, s):
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}   # close -> matching open

        for ch in s:
            if ch in pairs:                       # closing bracket
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()                   # top matches → remove it
                else:
                    return False                  # mismatch or nothing to close
            else:                                 # opening bracket
                stack.append(ch)

        return len(stack) == 0                     # valid only if stack is empty