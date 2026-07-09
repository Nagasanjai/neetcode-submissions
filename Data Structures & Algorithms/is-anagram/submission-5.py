class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        reversed_str = s[::-1]
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i],0)+1
            t_count[t[i]] = t_count.get(t[i],0)+1
        if s_count == t_count:
            return True
        else:
            return False
