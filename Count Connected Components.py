class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n: #stupid little edge case
            return 0

        components = {i:[] for i in range(n)}
        for n1, n2 in edges:
            components[n1].append(n2)
            components[n2].append(n1)
        
        visit = set()
        count = 0

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in components[node]:
                dfs(nei)
        for c in range(n):
            if c not in visit:
                count +=1
                dfs(c)
        #return count
        return count

            