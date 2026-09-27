"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        maping = {}

        def dfs(node):
            if node in maping:
                return maping[node]
            
            maping[node] = Node(node.val)
            for nei in node.neighbors:
                maping[node].neighbors.append(dfs(nei))
            return maping[node]
        
       
        return dfs(node) if node else None