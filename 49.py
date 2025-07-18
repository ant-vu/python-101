class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time: O(nlogn), space: O(n)
        mapping = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in mapping:
                mapping[key] = [s]
            else:
                mapping[key].append(s)
        return list(mapping.values())