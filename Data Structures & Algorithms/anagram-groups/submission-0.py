class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            sort = ''.join(sorted(i))
            res[sort].append(i)
        return list(res.values())


