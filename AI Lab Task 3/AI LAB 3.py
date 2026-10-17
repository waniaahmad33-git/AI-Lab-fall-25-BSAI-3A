
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start = 'A'
goal = 'G'


def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path

    if limit == 0:
        if graph[node]:
            return "CUTOFF", None
        return "FAILURE", None

    cutoff_found = False

    for child in graph[node]:
        if child not in path:
            status, result_path = dls(
                child, goal, limit - 1, path + [child]
            )

            if status == "FOUND":
                return status, result_path

            if status == "CUTOFF":
                cutoff_found = True

    if cutoff_found:
        return "CUTOFF", None

    return "FAILURE", None


def iddfs(start, goal, max_depth):
    attempted_limits = []

    for limit in range(1, max_depth + 1):
        attempted_limits.append(limit)

        status, path = dls(start, goal, limit, [start])

        if status == "FOUND":
            return status, path, attempted_limits

        if status == "FAILURE":
            return status, None, attempted_limits

    return "CUTOFF", None, attempted_limits


print("DLS Results")

for limit in range(1, 5):
    status, path = dls(start, goal, limit, [start])

    if path is None:
        path_text = "No solution"
    else:
        path_text = " -> ".join(path)

    print("Limit:", limit,
          "| Status:", status,
          "| Path:", path_text)


print("\nIDDFS Results")

for max_depth in range(1, 5):
    status, path, attempted = iddfs(
        start, goal, max_depth
    )

    if path is None:
        path_text = "No solution"
    else:
        path_text = " -> ".join(path)

    print("Maximum depth:", max_depth,
          "| Status:", status,
          "| Path:", path_text,
          "| Limits attempted:", attempted)
