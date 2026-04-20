class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        for c in s:
            s_dict[c]=s_dict.get(c,0)+1

        for c in t:
            s_dict[c]=s_dict.get(c,0)-1
            if s_dict[c]<0:
                return False

        for v in s_dict.values():
            if v!=0:
                return False

        return True
