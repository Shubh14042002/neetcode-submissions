import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = re.sub(r"[^a-zA-Z0-9 ]", "", s)
        clean_text = clean_text.replace(" ","").lower()
        print(clean_text)
        txt_arr = ""
        i = len(clean_text) - 1
        while i >=0 :
            txt_arr+=clean_text[i]
            i-=1
        if txt_arr == clean_text :
            return True
        else:
            return False