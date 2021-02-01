from typing import List


class FindTheMostCompetitiveSubsequence:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack=[]
        numDeletions=len(nums)-k

        for num in nums:
            while stack and stack[-1]>num and numDeletions>0:
                numDeletions-=1
                stack.pop()
            stack.append(num)

        for _ in range(numDeletions):
            stack.pop()
        return stack



if __name__ == '__main__':
    init = FindTheMostCompetitiveSubsequence()
    print(init.mostCompetitive(nums = [3,5,2,6], k = 2)) #[2,6]
    #print(init.mostCompetitive(nums = [2,4,3,3,5,4,9,6], k = 4)) #[2,3,3,4]
