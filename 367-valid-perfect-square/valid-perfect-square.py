class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return True

        lo = 0 
        hi = num

        while lo != hi:
            mid = (lo + hi) //2
            exp = mid*mid
            if exp == num:
                return True
            elif exp > num:
                hi = mid
            else:
                lo = mid+1

        return False
