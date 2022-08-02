# given two binary strings a and b, return their sum as a binary string

# input: a = "11", b = "1"
# output: "100"

# intput: a = "1010", b = "1011"
# output: "10101"

# class Solution: #??????????
#     def addBinry(self, a, b):
#         res = ""
#         i, j, carry - len(a) - 1, len(b) - 1, 0
#         while i >= 0 or j >= 0:
#           sum = carry;
#           if i >= 0: sum += ord(a[i]) - ord('0') # ord is use to get value of ACSII character
#           if j >= 0: sum += ord(b[j]) - ord('0')
#           i, j = i - 1, j - 1
#           carry = 1 if sum > 1 else 0;
#           res += str(sum % 2)
        
#         if carry != 0 : res += str(carry);
#         return res[::-1]

# linear algorithm

# class Solution: # this only works for the first one 
#     def addBinary(self, a: str, b: str) -> str:
#         res = ""
#         carry = 0

#         a, b = a[::-1], b[::-1]

#         for i in range(max(len(a), len(b))):
#             digitA = ord(a[i]) - ord("0") if i < len(a) else 0
#             digitB = ord(b[i]) - ord("0") if i < len(b) else 0 

#             total = digitA + digitB + carry 
#             char = total % 2 

#             total = 2
#             char = str(total % 2)
#             res = char + res 
#             carry = total // 2
        
#         if carry: 
#             res = "1" + res 
#         return 

# a = "1010"
# b = "1011"
# ob1 = Solution()
# print(ob1.addBinary(a, b))

class Solution:
    def addBinary(self, a, b):
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            
            result += str(carry % 2)
            carry //= 2

        return result[::-1]

a = "11"
b = "1"
ob1 = Solution()
print(ob1.addBinary(a, b))