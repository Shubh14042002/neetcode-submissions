class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        res = defaultdict(list) # map charCount to List of Anagrams
        for x in strs:
            count = [0]*26
            for char in x:
                count[ord(char)-ord('a')] = count[ord(char)-ord('a')] + 1
            res[tuple(count)].append(x)
            
        return list(res.values())