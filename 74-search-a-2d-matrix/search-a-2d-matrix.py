class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def search(arr, target):
            l, r = 0, len(arr)-1

            while l <= r:
                m = (l+r)//2
                if arr[m] == target:
                    return True
                
                if target > arr[m]:
                    l = m+1

                if target < arr[m]:
                    r = m-1
            return False

        for i in range(len(matrix)):
            if matrix[i][0] == target or matrix[i][-1] == target:
                return True
            if target > matrix[i][0] and target < matrix[i][-1]:
                return search(matrix[i], target)