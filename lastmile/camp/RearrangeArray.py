class RearrangeArray:
    def rearrangeArray(self, arr):
        curr, right = 0, len(arr) - 1
        while curr <= right:
            if arr[curr] == 0:
                curr += 1
            else:
                arr[curr], arr[right] = arr[right], arr[curr]
                right-=1
        return arr


if __name__ == '__main__':
    init = RearrangeArray()
    print(init.rearrangeArray([4, 2, 0, 1, 0, 3, 0]))
