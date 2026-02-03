class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        n = len(nums)
        
        # Lower Bound: First occurrence
        left, right = 0, n - 1
        lb = n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                lb = mid
                right = mid - 1
            else:
                left = mid + 1
        
        # Upper Bound: First position > target
        left, right = 0, n - 1
        ub = n
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:  # Only change: > instead of >=
                ub = mid
                right = mid - 1
            else:
                left = mid + 1
        
        # Check if target exists
        if lb <= ub - 1:
            return [lb, ub - 1]
        
        return [-1, -1]