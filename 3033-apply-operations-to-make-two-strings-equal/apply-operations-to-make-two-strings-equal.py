class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        diff = [i for i in range(len(s1)) if s1[i] != s2[i]]

        if len(diff) % 2 != 0:
            return -1
        if len(diff) == 0:
            return 0

        prev, curr = 0, min(diff[1]-diff[0], x)
        for i in range(2, len(diff)):
            if i % 2 == 0:
                prev, curr = curr, min(curr, prev+min(diff[i]-diff[i-1], x))
            else:
                prev, curr = curr, min(curr+x, prev+min(diff[i]-diff[i-1], x))
        return curr