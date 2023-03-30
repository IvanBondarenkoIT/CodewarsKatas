class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        answer = True
        left_border = 0
        for i in s:
            if t[left_border:].find(i) == -1:
                return False
            else:
                left_border = t[left_border:].find(i)+1

        return answer


s = Solution()
print(s.isSubsequence(s="abc", t="ahbgdc"))
print(s.isSubsequence(s="axc", t="ahbgdc"))
print(s.isSubsequence(s="aaaaaa", t="bbaaaa"))
print(s.isSubsequence(s="ab", t="baab"))

