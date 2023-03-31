class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        coincidence = 0
        for i in range(len(t)):
            if coincidence <= len(s) - 1:
                if s[coincidence] == t[i]:
                    coincidence += 1

        return coincidence == len(s)


s = Solution()
print(s.isSubsequence(s="abc", t="ahbgdc"))
print(s.isSubsequence(s="axc", t="ahbgdc"))
print(s.isSubsequence(s="aaaaaa", t="bbaaaa"))
print(s.isSubsequence(s="ab", t="baab"))

