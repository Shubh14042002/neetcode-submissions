class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ###third dolution using a single fixed array 
        count = [0]*26
        if len(s) != len(t):
            return False
        else :
            for char in s:
                count[ord(char)-ord('a')] = count[ord(char)-ord('a')] + 1
            for char in t:
                 count[ord(char)-ord('a')] = count[ord(char)-ord('a')] - 1

            for val in count:
                if val != 0 :
                    return False
            return True 