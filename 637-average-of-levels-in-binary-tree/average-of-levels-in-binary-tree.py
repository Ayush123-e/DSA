# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dq = deque()
        dq.append(root)
        result = []
        while dq:
            arr = []
            length = len(dq)
            for i in range(length):
                ele = dq.popleft()
                arr.append(ele.val)
                if ele.left:
                    dq.append(ele.left)
                if ele.right:
                    dq.append(ele.right)
            result.append(sum(arr) / len(arr))
        return result