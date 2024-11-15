import numpy as np
import matplotlib.pyplot as plt

def find_clusters(grid):
    # Define the directions for up, down, left, and right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Function to check if a cell is within the grid and contains a 1
    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1
    
    # DFS function to find a cluster
    def dfs(x, y, visited, cluster):
        # Mark the current cell as visited
        visited[x][y] = 1
        
        # Initialize the cluster with the current cell
        cluster[x][y] = 1
        
        # Try each direction
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and not visited[nx][ny]:
                # Find the cluster in the direction
                dfs(nx, ny, visited, cluster)
                        
        return cluster
    
    # Create a copy of the grid to mark visited cells
    visited = [[0 for col in grid[0]] for row in grid]
    
    # Initialize the list of clusters
    clusters = []
    
    # Start DFS from each cell that contains a 1
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1 and not visited[i][j]:
                cluster = [[0 for col in grid[0]] for row in grid]
                cluster = dfs(i, j, visited, cluster)
                clusters.append(cluster)
    
    return clusters

def percolating_cluster(clusters):
    perc_cluster_list_location = []
    for cluster_number, cluster in enumerate(clusters):
        perc_start = False
        perc_end = False
        for i, row in enumerate(cluster):
            if row[0] == 1:
                perc_start = True
            if row[-1] == 1:
                perc_end = True
        if perc_start and perc_end:
            perc_cluster_list_location.append(cluster_number)
    return perc_cluster_list_location

def cluster_size_list(clusters):
    size_list  = {}
    for cluster in clusters:
        size = sum(np.matrix(cluster).A1)
        key = f"n = {size}"
        if key not in size_list:
            size_list[key] = 1
        else:
            size_list[key] += 1
    size_list
    return size_list


grid = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1]
]

clusters = find_clusters(grid)
size_list = cluster_size_list(clusters)
print(size_list)
names = size_list.keys()
names = [key for key in names]
plt.bar(range(len(size_list)), size_list.values(), names)
plt.xticks(rotation=20)




    
        
