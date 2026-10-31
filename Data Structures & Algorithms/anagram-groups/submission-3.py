class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        sortLetters = defaultdict(list)
        for s in strs:
            sortS = ''.join(sorted(s))
            sortLetters[sortS].append(s)
        return list(sortLetters.values())
       

        