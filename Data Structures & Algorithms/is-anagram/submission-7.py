class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False 
        count_map_s = {}
        count_map_t = {}
        for char in s:
            count_map_s[char] = count_map_s.get(char,0)+1
        for char in t:
            count_map_t[char] = count_map_t.get(char,0)+1

        if count_map_s == count_map_t :
            return True
        else :
            return False