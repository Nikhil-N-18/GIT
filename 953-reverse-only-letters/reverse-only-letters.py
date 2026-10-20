class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = list(s)
        start,end = 0,len(arr)-1
        while start < end:
            if arr[start].isalpha() and arr[end].isalpha():
                arr[start],arr[end] = arr[end],arr[start]
                start += 1
                end -=1
            elif not arr[start].isalpha():
                start += 1
            else:
                end -= 1
        return ''.join(arr)