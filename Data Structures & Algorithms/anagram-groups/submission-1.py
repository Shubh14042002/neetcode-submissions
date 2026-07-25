class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        length_List = len(strs)
        print(length_List)
        grouped_List = []
        i = 0
        skip_index_List = []
        while i < length_List :
            # skip the index of a successful match
            if i in skip_index_List : 
                i+=1
                continue
            sorted_sub_List = [] # clear sub list 
            sorted_sub_List.append(strs[i])
            sorted_word = sorted(strs[i])
            j = i+1 
            while j < length_List :
                if sorted_word == sorted(strs[j]):
                    sorted_sub_List.append(strs[j])
                    skip_index_List.append(j)
                j+=1
            grouped_List.append(sorted_sub_List)
            i+=1
        return grouped_List



