# given two strings ransomNote and magazine, return true IF ransomNote can be constructed by using the letters from magazine and false otherwise.

# each letter in magazine can only be used once in ransomNote

# input: ransomNote = "a", magazine = "b"
# output: false 

# input: ransomNote = "aa", magazine = "ab"
# output: false 

# input: ransomNote = "aa", magazine = "aab"
# output: true 

from collections import Counter 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineKeyCount = Counter(magazine)

        for val in ransomNote:
            if val in magazineKeyCount and magazineKeyCount[val] > 0:
              # drop one count for val
              magazineKeyCount[val] -= 1
            else:
              # no such letter exists in magazine
              return False
        return True 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        for key in ransomNote:
            if key not in magazine.keys():
                return False 
            if ransomNote[key] > magazine[key]:
                return False 
        return True 

ransomNote = "aa"
magazine = "aab"
ob1 = Solution()
print(ob1.canConstruct(ransomNote, magazine))