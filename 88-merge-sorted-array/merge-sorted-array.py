class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:]=[]
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()

    


