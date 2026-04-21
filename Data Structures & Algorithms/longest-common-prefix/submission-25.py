def the_funct(strs: List[str], the_chain=''):
    the_dict = {}
    for word in strs:
        if word.startswith(the_chain) and len(word) > len(the_chain):
            the_dict[word[:len(the_chain)+1]] = the_dict.get(word[:len(the_chain)+1], 0) + 1
    
    if not the_dict or the_dict[max(the_dict, key=the_dict.get)] < len(strs):
        return the_chain
    else:
        the_chain = max(the_dict, key=the_dict.get)
        return the_funct(strs, the_chain)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return the_funct(strs, '')