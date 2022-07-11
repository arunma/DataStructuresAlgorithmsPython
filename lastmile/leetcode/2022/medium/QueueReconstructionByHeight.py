from typing import List


class QueueReconstructionByHeight:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        result=[]
        for p in people:
            result.insert(p[1], p)
        return result


if __name__ == '__main__':
    init = QueueReconstructionByHeight()
    print(init.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])) #[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
