class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=list(range(0,n+1))
        rank=[0 for i in range(0,n+1)]
        print(parent)


        def findParent(x):
            print(x)
            if parent[x]==x:
                return x
            parent[x]=findParent(parent[x])
            return parent[x]
        def add(x,y):
            rootX,rootY=findParent(x),findParent(y)
            if rootX==rootY:
                return True
            if rank[rootX]>rank[rootY]:
                parent[rootY]=parent[rootX]
            elif rank[rootX]<rank[rootY]:
                parent[rootX]=parent[rootY]
            else:
                rank[rootX]+=1
                parent[rootY]=parent[rootX]
            return False
        for i,j in edges:
            if add(i,j):
                return [i,j]
        return []
        
        