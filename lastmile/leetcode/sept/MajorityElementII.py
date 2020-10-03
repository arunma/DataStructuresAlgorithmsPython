from typing import List


class MajorityElementII:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1=0
        count2=0
        cand1=None
        cand2=None

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1==0:
                cand1, count1=num, 1
            elif count2==0:
                cand2, count2=num, 1
            else:
                count1-=1
                count2-=1

        result=[]
        for cand in [cand1, cand2]:
            if nums.count(cand)>len(nums)//3:
                result.append(cand)
        return result




if __name__ == '__main__':
    init = MajorityElementII()
    print(init.majorityElement([3,2,3])) #[3]
    print(init.majorityElement([1])) #[1]
    print(init.majorityElement([1,2])) #[1,2]
    print(init.majorityElement([2,2])) #[1,2]
