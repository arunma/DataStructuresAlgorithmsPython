import bisect


class TraversingArrayInReverse:
    def cloneEvenNumbers(self, arr):
        act_end = arr.index(-1) -1
        arr_end=len(arr)-1

        while arr_end>0:
            if arr[act_end]%2==0:
                arr[arr_end]=arr[act_end]
                arr_end-=1

            arr[arr_end] = arr[act_end]
            arr_end -= 1

            act_end-=1


        #
        # while act_end >= 0:
        #     if arr[arr_end % 2] == 0:
        #         arr[arr_end] = arr[act_end]
        #         arr_end -= 1
        #         arr[arr_end] = arr[act_end]
        #         arr_end -= 1
        #     else:
        #         arr[arr_end] = arr[act_end]
        #         arr_end -= 1
        #     act_end -= 1
        return arr


if __name__ == '__main__':
    init = TraversingArrayInReverse()
    print(init.cloneEvenNumbers([4, 2, 5, 6, 8, -1, -1, -1, -1]))  # 1,2,2,5,6,6,8,8]
