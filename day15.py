from queue import PriorityQueue

# prep data
map = []
with open('input15.txt') as f:
    for line in f.read().splitlines():
        map.append([int(char) for char in line])


# part 2 map
def bigMap(map):
    # TODO: optimize this using a template matrix with the correct multipliers
    #       and expand the original map using that
    # expand to right
    bm = []
    long_map = map.copy()
    # extend map horizontally
    for i in range(4):
        pasted_map = []
        for row in map:
            new_row = []
            for num in row:
                if num == 9:
                    new_row.append(1)
                else:
                    new_row.append(num+1)
            pasted_map.append(new_row)
        bm.append(pasted_map)
        map = pasted_map[:]
    for map in bm:
        for index, row in enumerate(map):
            for num in row:
                long_map[index].append(num)
    # extend map vertically
    big_map = long_map.copy()
    for i in range(4):
        for row in long_map:
            lrow = []
            for num in row:
                num += 1 + i
                if num > 9:
                    lrow.append(num % 9)
                else:
                    lrow.append(num)
            big_map.append(lrow)

    return big_map


# first time learning about dijkstra's; need to make more efficient
# part 2 takes like an hour to run lol
def dijkstra(start_vertex, map):
    visited = []
    D = {}
    for ri, r in enumerate(map):
        for ci, c in enumerate(r):
            D[(ri, ci)] = float('inf')
    D[start_vertex] = 0
    end = (len(map)-1, len(map)-1)
    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while pq:
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)
        neighbors = getNeighbors(current_vertex, map)
        for neighbor in neighbors:
            distance = map[neighbor[0]][neighbor[1]]
            if neighbor not in visited:
                old_cost = D[neighbor]
                new_cost = D[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    D[neighbor] = new_cost
                    if neighbor == end:
                        return new_cost

    return D[end]


def getNeighbors(cv, map):
    row = cv[0]
    col = cv[1]
    poss_neighbors = [(row + 1, col), (row - 1, col), (row, col + 1),
                      (row, col - 1)]
    # create list of valid neighbors
    valid_neighbors = []
    for v in poss_neighbors:
        if isValid(v, map):
            valid_neighbors.append(v)
    return valid_neighbors


def isValid(coord, map):
    row = coord[0]
    col = coord[1]
    max_row = len(map)
    max_col = len(map)
    if (row < 0 or col < 0 or row >= max_row or col >= max_col):
        return False
    return True


# uncomment for part 2
# map = bigMap(map)
D = dijkstra((0, 0), map)

print(D)
