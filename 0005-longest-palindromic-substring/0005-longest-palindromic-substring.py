class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        
        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome
            return right - left - 1

        for i in range(len(s)):
            # Odd length palindromes (single character center)
            len1 = expand_around_center(i, i)
            # Even length palindromes (two character center)
            len2 = expand_around_center(i, i + 1)
            
            max_len = max(len1, len2)
            
            # Update start and end indices if a longer palindrome is found
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]
