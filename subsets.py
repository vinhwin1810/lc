class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start, subset):
            """
            If you simply append subset directly to res without making a copy, 
            all the references in res will point to the same subset list. 
            Since subset is modified in place during the recursion (elements are added and removed), 
            all entries in res would eventually reflect the same (final) state of subset, 
            which would likely be an empty list after all elements have been removed due to backtracking.
            """
            res.append(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])
                dfs(i+1, subset)
                subset.pop()
            
        dfs(0, [])
        return res
