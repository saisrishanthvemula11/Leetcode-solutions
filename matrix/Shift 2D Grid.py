class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        data = [element for row in grid for element in row]
        n = len(data)
        start = n - k % n
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = data[start % n]
                start +=1
        return grid 
        

        