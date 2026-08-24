import bisect

class TimeMap:

    def __init__(self):
        # Maps key -> list of [timestamp, value]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        pairs = self.store[key]
        
        # Binary search for the correct timestamp position
        # bisect_right looks for the index where 'timestamp' would fit to the right
        # We pass [timestamp, chr(127)] to safely compare against [timestamp, value]
        idx = bisect.bisect_right(pairs, [timestamp, chr(127)])
        
        # If idx is 0, all stored timestamps are strictly greater than the requested one
        if idx == 0:
            return ""
            
        return pairs[idx - 1][1]

