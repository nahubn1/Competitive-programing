class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated = ""
        for char in s:
            if char.isalpha():updated += char.lower()
            elif char.isdigit(): updated += char
        return True if  updated == ''.join(reversed(updated)) else False
