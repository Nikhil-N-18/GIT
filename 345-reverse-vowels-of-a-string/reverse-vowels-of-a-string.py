class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel = ("aeiouAEIOU")
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left] not in vowel:
                left += 1
            elif s[right] not in vowel:
                right -= 1
            else:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                right -=1
                left += 1
        return "".join(s)
            

        