inputGraph = {
    'A': [('B', 5), ('D', 12)],
    'B': [('A', 9), ('C', 4)],
    'C': [('D', 4), ('B', 7)],
    'D': [('A', 9), ('C', 5)]
}

goal = "D"

def gbfs(graph, start):
    queue = [(start, 0)]  # Queue stores (node, heuristic_cost)
    visitedNode = []

    while queue:
        queue.sort(key=lambda x: x[1])  # Sort by heuristic cost
        node, _ = queue.pop(0)

        if node not in visitedNode:
            visitedNode.append(node)

            if node == goal:
                break

            neighbours = graph[node]
            for neighbour, cost in neighbours:
                queue.append((neighbour, cost))  # Assume cost is the heuristic

    return visitedNode

def calculate_path_cost(visited_nodes):
    path_cost = 0
    for i in range(len(visited_nodes) - 1):
        current_node = visited_nodes[i]
        next_node = visited_nodes[i + 1]
        for neighbor, cost in inputGraph[current_node]:
            if neighbor == next_node:
                path_cost += cost
                break
    return path_cost

result = gbfs(inputGraph, "A")  # Start from node "A"
print("Visited Nodes:")
print(result)
print("Total Path Cost:", calculate_path_cost(result))