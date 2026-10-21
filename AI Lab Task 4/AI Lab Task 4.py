
import heapq

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

h = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}


def astar(graph, h, start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}
    processed = []
    expanded = []

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if g != best[node]:
            print("Stale entry ignored:", node)
            continue

        processed.append(node)
        print("Processed:", node, "g =", g, "h =", h[node],
              "f =", g + h[node])

        if node == goal:
            return path, g, processed, expanded

        expanded.append(node)

        for nxt, w in graph[node]:
            ng = g + w

            if ng < best.get(nxt, float("inf")):
                best[nxt] = ng
                heapq.heappush(
                    pq, (ng + h[nxt], ng, nxt, path + [nxt])
                )

    return [], float("inf"), processed, expanded


print("A* SEARCH")
a_path, a_cost, a_processed, a_expanded = astar(
    graph, h, "S", "G"
)

print("\nUCS SEARCH")
zero_h = {"S": 0, "A": 0, "B": 0, "C": 0, "G": 0}

u_path, u_cost, u_processed, u_expanded = astar(
    graph, zero_h, "S", "G"
)


print("\nFINAL RESULTS")

print("A* Path:", a_path)
print("A* Cost:", a_cost)
print("A* Processed:", a_processed)
print("A* Expanded:", a_expanded)
print("A* Expansion Count:", len(a_expanded))

print("\nUCS Path:", u_path)
print("UCS Cost:", u_cost)
print("UCS Processed:", u_processed)
print("UCS Expanded:", u_expanded)
print("UCS Expansion Count:", len(u_expanded))
