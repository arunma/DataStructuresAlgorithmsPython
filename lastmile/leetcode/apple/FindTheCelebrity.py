from collections import defaultdict, Counter

graph = {}
# graph[0] = [1,1]
# graph[1] = [1,1]

# graph[0] = [1,1,0]
# graph[1] = [0,1,0]
# graph[2] = [1,1,1]

graph[0] = [1,0,0]
graph[1] = [1,1,1]
graph[2] = [1,0,1]

def knows(a: int, b: int) -> bool:
    return graph[a][b]==1

class FindTheCelebrity:
    # def findCelebrity(self, n: int) -> int:
    #     celeb_counter=Counter()
    #     non_celebs=set()
    #
    #     for i in range(n):
    #         for j in range(n):
    #             if i != j and knows(i, j):
    #                 non_celebs.add(i)
    #                 celeb_counter[j]+=1
    #
    #     for celeb in range(n):
    #         if celeb not in non_celebs and celeb_counter[celeb]== n - 1:
    #             return celeb
    #     return -1

    def findCelebrity(self, n: int) -> int:
        left=0
        right=n-1

        while left<right:
            if knows(left, right):
                left+=1
            else:
                right-=1

        for i in range(n):
            if i!=left and knows (left, i ) or not knows(i, left):
                return -1

        return left


if __name__ == '__main__':
    init = FindTheCelebrity()
    print(init.findCelebrity(3)) #-1
