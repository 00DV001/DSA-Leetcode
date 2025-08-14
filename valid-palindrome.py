#https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        temp = ''
        temp2 = ''
        for i in s:
            if i.isalnum():
                temp += i
        print(temp)
        s_rev = ''.join(reversed(s))
        for j in s_rev:
            if j.isalnum():
                temp2+=j
        print(temp2)
        return True if temp == temp2 else False