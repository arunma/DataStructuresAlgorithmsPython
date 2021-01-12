from typing import List


class CheckArrayFormationThroughConcatenation:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pmap={piece[0]: piece for piece in pieces}
        result=[]
        for num in arr:
            result+=pmap.get(num, [])
        return result==arr





if __name__ == '__main__':
    init = CheckArrayFormationThroughConcatenation()
    print(init.canFormArray(arr = [91,4,64,78], pieces = [[78],[4,64],[91]])) #True
    print(init.canFormArray(arr = [15,88], pieces = [[88],[15]])) #True
    print(init.canFormArray(arr = [85], pieces = [[85]])) #True
    print(init.canFormArray(arr = [1,3,5,7], pieces = [[2,4,6,8]])) #False
    print(init.canFormArray(arr = [49,18,16], pieces = [[16,18,49]])) #False
