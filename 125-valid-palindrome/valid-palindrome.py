class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        reversed_s = s[::-1]
        if s == reversed_s:
            return True
        else:
            return False