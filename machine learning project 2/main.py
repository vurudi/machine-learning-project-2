from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(lambda: defaultdict(int))
        self.V = vertices

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def dfs(self, u, t, visited, path):
        visited[u] = True
        path.append(u)

        if u == t:
            return True

        for v in self.graph[u]:
            if not visited[v] and self.graph[u][v] > 0:
                if self.dfs(v, t, visited, path):
                    return True

        path.pop()
        return False

    def ford_fulkerson(self, source, sink):
        print("Calculating maximum flow")
        max_flow = 0

        while True:
            visited = {v: False for v in range(self.V)}
            path = []
            if not self.dfs(source, sink, visited, path):
                break

            path_flow = float("inf")
            s = path[0]
            for v in path[1:]:
                if self.graph[s][v] < path_flow:
                    path_flow = self.graph[s][v]
                s = v

            max_flow += path_flow

            s = path[0]
            for v in path[1:]:
                self.graph[s][v] -= path_flow
                self.graph[v][s] += path_flow
                s = v

        return max_flow


if __name__ == '__main__':
    print("program is starting")
    g = Graph(6)
    g.add_edge(0, 1, 16)
    g.add_edge(0, 2, 13)
    g.add_edge(1, 2, 10)
    g.add_edge(2, 1, 4)
    g.add_edge(1, 3, 12)
    g.add_edge(2, 4, 14)
    g.add_edge(3, 2, 9)
    g.add_edge(3, 5, 20)
    g.add_edge(4, 3, 7)
    g.add_edge(4, 5, 4)

    source = 0
    sink = 5

    max_flow = g.ford_fulkerson(source, sink)

    print("Maximum flow:", max_flow)
