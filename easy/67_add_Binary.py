class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l_a, l_b = len(a), len(b)

        if l_a < l_b:
            a = a.zfill(l_b)
            l_a = len(a)
        else:
            b = b.zfill(l_a)

        print(a,b)
        carry = 0
        s = ""

        for i in range(l_a - 1, -1, -1):
            if a[i] == "1" and b[i] == "1":
                s = str(carry) + s
                carry = 1
            elif a[i] == "0" and b[i] == "0":
                s = str(carry) + s
                carry = 0
            elif ((a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0")) and carry == 0:
                s = "1" + s
            elif ((a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0")) and carry == 1:
                s = "0" + s

        if carry == 1:
            s = "1" + s

        return s

if __name__ == "__main__":
    print(Solution().addBinary("1", "111111"))