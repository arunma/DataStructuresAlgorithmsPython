class ReverseTheOrderOfElements:
    def reverse(self, arr):
        left=0
        right=len(arr)-1
        while left<right:
            arr[left], arr[right]=arr[right], arr[left]
            left+=1
            right-=1
        return arr



if __name__ == '__main__':
    init = ReverseTheOrderOfElements()
    print(init.reverse([3,5,2,5,2,3,9])) #→ [9,3,2,5,2,5,3]
