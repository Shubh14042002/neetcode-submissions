class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # substring_1 = []
        # substring_2 = []
        # char = None
        # switch = False
        # print("start")
        # for i in range(len(s)):
        #     if char is None:    
        #         char = s[0]
        #         substring_1.append(char)
        #         print("first char added"+" "+ s[i])

        #     elif s[i] not in substring_1 and switch == False:
        #         substring_1.append(s[i])
        #         print("appended substring_1")

        #     elif s[i] in substring_1 and switch == False :
        #         substring_2.append(s[i])
        #         switch = True
        #         print("started substring_2")

        #     elif s[i] not in substring_2 and switch == True:
        #         substring_2.append(s[i])
        #         print("appended substring_2")

        #     elif s[i] in substring_2 and switch == True:
        #         if len(substring_2) > len(substring_1):
        #             substring_1 = substring_2
        #             substring_2 = []
        #             substring_2.append(s[i])
        #             print("found bigger substring2")

        #         else:
        #             substring_2 = []
        #             substring_2.append(s[i])
        #             print("substring one is bigger we use that")
        
        # if len(substring_2) > len(substring_1):
        #     return len(substring_2)
        # else:
        #     return len(substring_1)
            
        # problem with above solution is it starts a new list upon a repeated letter and doesnt account for the chars after .


        # substring = []
        # best = 0 
        # for char in s:
        #     while char in substring:
        #         substring.pop(0)
        #     substring.append(char)
        #     if len(substring) > best:
        #         best = len(substring)
        # return best

        # solution is right but too memory expensive and slow . for char in s and .pop are slow 

        ## next solution : use sets intead of using list, and use two variables as pointers to keep track of the indexes .(left ptr for shrinking and right ptr for adding ) 

        chars = set()
        left = 0 
        best = 0 

        for right in range(len(s)):
            while s[right] in chars:
                    chars.remove(s[left]) 
                    left += 1
            chars.add(s[right])
            if len(chars) > best:
                best = len(chars)
        return best
