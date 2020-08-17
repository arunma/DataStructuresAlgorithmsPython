class SearchInA2DMatrix:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            mat=matrix[i]
            if mat[0]<=target<=mat[C-1]:
                if self.binsearch(mat, target, 0, C-1):
                    return True
        return False

    def binsearch(self, mat, target, low, high):
        while low<=high:
            mid=low+(high-low)//2
            if mat[mid]==target:
                return True
            elif mat[low]<=target<mat[mid]:
                high=mid-1
            else:
                low=mid+1
        return False



if __name__ == '__main__':
    init = SearchInA2DMatrix()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(init.searchMatrix(matrix, 5)) #true
    print(init.searchMatrix(matrix, 20)) #false

