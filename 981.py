class TimeMap:  # time: O(nlogn), space: O(n)

    def __init__(self):
        self.maps = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.maps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.maps[key]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if self.maps[key][m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        return '' if l == 0 else self.maps[key][l - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)