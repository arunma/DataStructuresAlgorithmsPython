from typing import List


class BringZeroesToFront:
    def bring_zeros_to_front(self, nums: List[int]):
        # 1,3,0,0,4,0,5,8
        # numi
        # zeroi=0
        # For a non-zero number, i just increment numi
        # For a zero, I swap the value in numi with zeroi+1
        # Increment zeroi
        numi, zeroi = 0, -1
        while numi < len(nums):
            if nums[numi] != 0:
                numi += 1
            else:
                nums[numi], nums[zeroi + 1] = nums[zeroi + 1], nums[numi]
                zeroi += 1
                numi += 1

        return nums


if __name__ == '__main__':
    init = BringZeroesToFront()
    print(init.bring_zeros_to_front([1, 3, 0, 0, 4, 0, 5, 8]))  # 0,0,0,1,3,4,5,8
