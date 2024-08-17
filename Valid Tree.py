class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # trees and graphs: trees cannot have a loop, and all the nodes must be connected.
        # algo, how to check
        # dfs on nodes that connected to the first node  => check how many nodes in the visited set
        # check visit {cycle needs to check condition for parent too} 

        treeMap = {i:[] for i in range(n)} #initialize Graph
        for node1, node2 in edges:
            treeMap[node1].append(node2)
            treeMap[node2].append(node1) #complete the graph as an adj list
        
        visit = set()

        def dfs(node, prev): #chek for cycle
            if node in visit:
                return False
            
            visit.add(node)
            for nei in treeMap[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n



        


