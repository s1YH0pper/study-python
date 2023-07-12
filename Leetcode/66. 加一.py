class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        l = []
        for i in digits:
            s += str(i)
        for i in str(int(s) + 1):
            l.append(int(i))
        return l
