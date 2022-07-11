from typing import List


class MaximumUnitsOnATruck:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        result = 0

        for box, unitsPerBox in boxTypes:
            if box <= truckSize:
                result += unitsPerBox * box
                truckSize -= box
            else:
                result += truckSize * unitsPerBox
                return result
        return result


if __name__ == '__main__':
    init = MaximumUnitsOnATruck()
    print(init.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4)) #8
    print(init.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10)) #91
