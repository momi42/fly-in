from collections import deque


class BFS:

    def find_path(
        self,
        graph,
        start,
        end,
    ):

        queue = deque()
        queue.append([start])
        visited = set()
        while queue:
            path = queue.popleft()
            current = path[-1]
            if current == end:
                return path
            if current in visited:
                continue
            visited.add(current)
            for neighbor in graph.neighbors(current):
                new_path = path.copy()
                new_path.append(neighbor)
                queue.append(new_path)
        return None
