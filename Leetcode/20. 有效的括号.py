class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):
            if s[i] in ["{", "[", "("]:
                stack.append(s[i])
            elif s[i] in ["}", "]", ")"] and stack:
                if stack[-1] + s[i] not in ["{}", "[]", "()"]:
                    return False
                else:
                    stack.pop()
            else:
                return False
            i += 1
        if stack:
            return False
        return True
