class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = float('inf')
        ans = 0
        for p in prices:
            if p < cur_min:
                cur_min = p
            ans = max(ans , p - cur_min)
        return ans

        
