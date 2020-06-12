from functools import cmp_to_key
from typing import List


class QueueReconstructionByHeight:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=cmp_to_key(lambda l1,l2: l2[0]-l1[0] if l1[0]!=l2[0] else l1[1]-l2[1]))
        result=[]
        for each in people:
            result.insert(each[1], each)
        return result


if __name__ == '__main__':
    init = QueueReconstructionByHeight()
    print(init.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
    print (init.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]])) #[[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]]
