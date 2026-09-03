class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        s = [0] * (l1 + l2)

        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):

                mul = int(num1[i]) * int(num2[j])
                summ = mul + s[i + j + 1]

                s[i + j + 1] = summ % 10
                s[i + j] += summ // 10
        
        for i, c in enumerate(s):
            if c != 0:
                break
        
        return "".join(map(str, s[i:]))
                