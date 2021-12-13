import networkx as nx
import matplotlib.pyplot as plt

# prep data with networkx
# (relatively inefficient for my solution but simple to implement & work with)
with open('input12.txt') as f:
    input = f.read().splitlines()

edges = []
for line in input:
    edges.append(line.split('-'))

G = nx.Graph()
G.add_edges_from(edges)

# uncomment to visualize graph
# visualize graph
# nx.draw(G, with_labels=True)
# plt.savefig("day12.png")


# brute force all possible paths that explore small caves once (or twice for pt2)
# keep track of unfinished paths using a stack
# part 1
def part1(G):
    stack = [['start']]
    completed_paths = []
    while stack:
        path = stack.pop()
        connections = list(G.adj[path[-1]])
        for node in connections:
            node_path = path.copy()
            if node.islower() and node in path:
                continue
            elif node == 'end':
                node_path.append(node)
                completed_paths.append(node_path)
            else:
                node_path.append(node)
                stack.append(node_path)

    return len(completed_paths)


# part 2
def part2(G):
    stack = [['start']]
    completed_paths = []
    while stack:
        path = stack.pop()
        double_small = False
        connections = list(G.adj[path[-1]])
        for node in connections:
            node_path = path.copy()
            # keep track of whenever the path already has 2 small caves
            for i in path:
                if i.islower() and path.count(i) == 2:
                    double_small = True

            if node.islower() and double_small and node in path:
                continue
            elif node == 'end':
                node_path.append(node)
                completed_paths.append(node_path)
            elif node != 'start':
                node_path.append(node)
                stack.append(node_path)
    return len(completed_paths)


print(part1(G))
print(part2(G))
