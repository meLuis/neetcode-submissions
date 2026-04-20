class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        for c in s:
            s_dict[c]=s_dict.get(c,0)+1

        for c in t:
            s_dict[c]=s_dict.get(c,0)-1

        return all(v==0 for v in s_dict.values())
