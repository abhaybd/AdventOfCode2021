def read_data(file):
    with open(file) as f:
        lines = f.read().split("\n")
    graph = {}
    for line in lines:
        a, b = line.split("-")
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_num_paths(graph, path, end, visited):
    if path[-1] == end:
        return 1

    node = path[-1]
    n_paths = 0
    for neighbor in graph[node]:
        if neighbor not in visited:
            if neighbor.islower():
                visited.add(neighbor)
            n_paths += find_num_paths(graph, path + [neighbor], end, visited)
            if neighbor.islower():
                visited.remove(neighbor)
    return n_paths


def main():
    graph = read_data("input.txt")
    n_paths = find_num_paths(graph, ["start"], "end", {"start"})
    print(n_paths)

main()
