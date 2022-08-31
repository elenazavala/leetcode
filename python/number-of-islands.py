class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        
        def bfs(r, c):
            q = collections.deque()
            
            q.append((r,c))
            visited.add((r,c))
            
            # get adjacents nodes
            # and mark them as visited
            directions = [[0,1], [0,-1], [-1,0], [1,0]]
            while q:
                #dequeue 
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and 
                    c in range(cols) and 
                    grid[r][c] == "1" 
                    and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))
                    
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
