
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = [[-1] * n for _ in range(m)]
        
        def dfs(row, col):
            if moves[row][col] != -1:
                return moves[row][col]
            
            max_move = 0
            directions = [(-1, 1), (0, 1), (1, 1)]
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] > grid[row][col]:
                    max_move = max(max_move, 1 + dfs(new_row, new_col))
            
            moves[row][col] = max_move
            return max_move
        
        max_moves = 0
        for row in range(m):
            max_moves = max(max_moves, dfs(row, 0))
        
        return max_moves
