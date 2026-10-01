class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        if len(s) != len(t) :
            return False
        else :
            # one naive solution would be to sort both the strings but sorting both s tring takes more time O nlog(n) so try another way?   
            for a in s :
                count_s[a] = count_s.get(a,0)+1 ## dict.get() method , get value at key a if it exists otherwise give 0 which is default value
            for b in t :
                count_t[b] = count_t.get(b,0)+1
            if count_s == count_t :
                return True
            else:
                return False
