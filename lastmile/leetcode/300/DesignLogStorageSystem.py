import bisect
from collections import defaultdict
from typing import List


class DesignLogStorageSystem:

    def __init__(self):
        self.store = {}
        self.idx_map = {'Year': 1, 'Month': 2, 'Day': 3, 'Hour': 4, "Minute": 5, "Second": 6}

    def put(self, id: int, timestamp: str) -> None:
        key = tuple(timestamp.split(":"))
        self.store[key] = id

    def retrieve(self, st: str, ed: str, gra: str) -> List[int]:
        idx = self.idx_map[gra]
        start = tuple(st.split(":")[:idx])
        end = tuple(ed.split(":")[:idx])
        result = []

        for key, value in self.store.items():
            rel_key = tuple(key[:idx])
            if start <= rel_key <= end:
                result.append(value)

        return result


if __name__ == '__main__':
    init = DesignLogStorageSystem()
    init.put(1, "2017:01:01:23:59:59")
    init.put(2, "2017:01:01:22:59:59")
    init.put(3, "2016:01:01:00:00:00")
    print(init.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00",
                        "Year"))  # return [1,2,3], because you need to return all logs within 2016 and 2017.
    print(init.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00",
                        "Hour"))  # return [1,2], because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.
