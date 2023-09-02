class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or len(self.store[key]) == 0:
            return ""
        values = self.store[key]
        l, r = 0, len(values) - 1
        while l < r:
            mid = (l + r) // 2
            if values[mid][-1] > timestamp:
                r = mid - 1
            elif values[mid][-1] < timestamp:
                l = mid + 1
            else:
                return values[mid][0]
        return values[l][0] if values[l][-1] < timestamp else ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)