class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        
        c1 = []
        c2 = []
        ans = []

        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    c1.append(i)
                    c2.append(j)

        for _ in range(len(c1)):
            ans.append(abs(c1[_] - c2[_]))


        return sum(ans)




