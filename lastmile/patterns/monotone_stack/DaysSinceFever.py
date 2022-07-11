import random
from typing import List


class DaysSinceFever:

#Given an array, `temps` that represents the daily body temperature of a person,
#return an array `answer` such that answer[i] is the number of days since the person has got fever.
#A person is considered to have fever if his body temperature exceeds 100 degree fahrenheit.
#If the person has never had fever, keep `answer[i]=-1`.

# Example 1
#Input: [100.11, 97.38, 99.77, 99.43, 97.35, 98.53]
#Output: [0, 1, 2, 3, 4, 5]

#Example 2
#Input: [99.09, 97.38, 100.11, 97.38, 99.77, 100.86, 97.77, 100.79]
#Output: [-1, -1, 0, 1, 2, 0, 1, 0]

#Example 3
#Input: [98.79, 97.07, 99.09, 100.11, 97.38, 99.77, 101.01, 100.3, 100.86, 97.77, 100.79]
#Output: [-1, -1, -1, 0, 1, 2, 0, 0, 0, 1, 0]

    def daysSinceFever(self, temps: List[int]) -> List[int]:
        N=len(temps)
        pge=[-1]*N
        stack=[]

        for i,temp in enumerate(temps):
            while stack and temps[stack[-1]]<temp:
                stack.pop()
            if stack:
                pge[i]=i-stack[-1]
            if temp>100:
                stack.append(i)
                pge[i]=0
        return pge



if __name__ == '__main__':
    init = DaysSinceFever()
    print(init.daysSinceFever([98.79, 97.07, 99.09, 100.11, 97.38, 99.77, 101.01, 100.3, 100.86, 97.77, 100.79]))
    #                               0       1       2       3      4      5      6      7
    print(init.daysSinceFever([99.09, 97.38, 100.11, 97.38, 99.77, 100.86, 97.77, 100.79]))
    print(init.daysSinceFever([100.11, 97.38, 99.77, 99.43, 97.35, 98.53]))
    y = [round(random.uniform(97, 102), 2) for x in range(1, 12)]
    print (y)
