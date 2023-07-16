class Solution:
    def addBinary(self, a: str, b: str) -> str:
        while len(a) > len(b):
            b = "0" + b
        while len(a) < len(b):
            a = "0" + a

        tmp = 0
        a, b = list(a), list(b)
        for i in range(len(a) - 1, -1, -1):
            cur = int(a[i]) + int(b[i]) + tmp
            if cur == 3:
                b[i] = "1"
                tmp = 1
            elif cur == 2:
                b[i] = "0"
                tmp = 1
            elif cur == 1:
                b[i] = "1"
                tmp = 0
            else:
                b[i] = "0"
                tmp = 0
        if tmp == 1:
            b = ["1"] + b
        return "".join(b)
