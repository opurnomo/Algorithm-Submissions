class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        sortLetter = defaultdict(list)
        for s in strs:
            sortS = "".join(sorted(s))
            sortLetter[sortS].append(s)
        return list(sortLetter.values())