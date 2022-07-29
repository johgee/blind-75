# given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character. 

# input: s = "ab#c", t = "ad#c"
# output: true 
# explanation: both s and t become "ac"

# input: s = "ab##", t = "c#d#"
# output: true
# explanation: both s and t become ""

# input: s = "a#c", t = "b"
# output: false 
# explanation: s becomes "c" while t becomes "b"

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            ans = []
            for c in s:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)

s = "ab#c"
t = "ad#c"
ob1 = Solution()
print(ob1.backspaceCompare(s, t))

# time complexity: O(M+N), M and N are the lengths of s and t 
# space complexity: O(M+N)