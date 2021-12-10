# prep data
with open('input9.txt') as f:
    input = f.read().splitlines()

heightmap = []
for row in input:
    temp_row = []
    for num in row:
        temp_row.append(int(num))
    heightmap.append(temp_row)

# part 1 / find low points / 2manyifstatements
max_row = len(heightmap)
max_col = len(heightmap[0])
low_points = []
low_coords = []
for row_index, row in enumerate(heightmap):
    for col_index, num in enumerate(row):
        # print(row_index, col_index)
        # corners
        if row_index == 0 and col_index == 0:
            if (num < heightmap[row_index + 1][col_index] and
                    num < heightmap[row_index][col_index + 1]):
                low_points.append(num)
                low_coords.append([row_index, col_index])
        elif row_index == 0 and col_index == max_col - 1:
            if (num < heightmap[row_index + 1][col_index] and
                    num < heightmap[row_index][col_index - 1]):
                low_points.append(num)
                low_coords.append([row_index, col_index])
        elif row_index == max_row - 1 and col_index == 0:
            if (num < heightmap[row_index - 1][col_index] and
                    num < heightmap[row_index][col_index + 1]):
                low_points.append(num)
                low_coords.append([row_index, col_index])
        elif row_index == max_row - 1 and col_index == max_col - 1:
            if (num < heightmap[row_index - 1][col_index] and
                    num < heightmap[row_index][col_index - 1]):
                low_points.append(num)
                low_coords.append([row_index, col_index])
        # edges
        elif row_index == 0 and col_index > 0 and col_index < max_col - 1:
            if (num < heightmap[row_index + 1][col_index] and
                num < heightmap[row_index][col_index - 1] and
                    num < heightmap[row_index][col_index + 1]):
                low_points.append(num)
                low_coords.append([row_index, col_index])
        elif row_index == max_row - 1 and col_index > 0 and col_index < max_col - 1:
            if (num < heightmap[row_index - 1][col_index] and
                num < heightmap[row_index][col_index - 1] and
                    num < heightmap[row_index][col_index + 1]):
                low_points.append(num)
                low_coords.append([row_index, col_index])
        elif col_index == 0 and row_index > 0 and row_index < max_row - 1:
            if (num < heightmap[row_index - 1][col_index] and
                num < heightmap[row_index + 1][col_index] and
                    num < heightmap[row_index][col_index + 1]):
                low_points.append(num)
                low_coords.append([row_index, col_index])
        elif col_index == max_col - 1 and row_index > 0 and row_index < max_row - 1:
            if (num < heightmap[row_index - 1][col_index] and
                num < heightmap[row_index + 1][col_index] and
                    num < heightmap[row_index][col_index - 1]):
                low_points.append(num)
                low_coords.append([row_index, col_index])
        # non-edge numbers
        else:
            if (num < heightmap[row_index - 1][col_index] and
                num < heightmap[row_index + 1][col_index] and
                num < heightmap[row_index][col_index - 1] and
                    num < heightmap[row_index][col_index + 1]):
                low_points.append(num)
                low_coords.append([row_index, col_index])

total_risk_level = sum(low_points) + len(low_points)

# part 2 / find size of basins
# learning about depth first search & trying to implement here
# https://www.geeksforgeeks.org/depth-first-traversal-dfs-on-a-2d-array/

# Initialize direction vectors
dRow = [0, 1, 0, -1]
dCol = [-1, 0, 1, 0]
vis = [[False for i in range(max_col)] for j in range(max_row)]


def isValid(row, col, grid):
    global max_row
    global max_col
    global vis

    # If cell is out of bounds
    if (row < 0 or col < 0 or row >= max_row or col >= max_col):
        return False

    # If the cell is already visited
    if (vis[row][col]):
        return False

    # If the cell = 9
    if grid[row][col] == 9:
        return False

    # Otherwise, it can be visited
    return True


def DFS(row, col, grid):
    global dRow
    global dCol
    global vis

    basin_cells = []
    # Initialize a stack of pairs and push the starting cell into it
    st = []
    st.append([row, col])

    # Iterate until the stack is not empty
    while (len(st) > 0):
        # Pop the top pair
        curr = st[len(st) - 1]
        st.remove(st[len(st) - 1])
        row = curr[0]
        col = curr[1]

        # Check if the current popped cell is a valid cell or not
        if (isValid(row, col, grid) == False):
            continue

        # Mark the current cell as visited
        vis[row][col] = True

        # add to list of basin cells
        basin_cells.append(grid[row][col])

        # Push all the adjacent cells
        for i in range(4):
            adjx = row + dRow[i]
            adjy = col + dCol[i]
            st.append([adjx, adjy])

    return(len(basin_cells))


size = []
for coord in low_coords:
    size.append(DFS(coord[0], coord[1], heightmap))
size.sort()

largest_multiplied = size[-3] * size[-2] * size[-1]

print(total_risk_level)
print(largest_multiplied)
