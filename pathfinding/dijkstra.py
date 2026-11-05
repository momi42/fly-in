import heapq


class Dijkstra:
    def _build_path(
            self,
            previous,
            start,
            end,
    ):
        path = [end]
        while path[-1] != start:
            path.append(previous[path[-1]])
        path.reverse()
        return path

    def find_path(
            self,
            graph,
            start,
            end,
    ):
        queue = []
        heapq.heappush(queue, (0, start))
        costs = {start: 0}
        previous = {}
        while queue:
            current_cost, current = (heapq.heappop(queue))
            if current == end:
                break
            for neighbor in graph.neighbors(current):
                zone = graph.get_zone(neighbor)
                new_cost = (current_cost + zone.cost())
                if (neighbor not in costs or new_cost < costs[neighbor]):
                    costs[neighbor] = new_cost
                    previous[neighbor] = current
                    heapq.heappush(queue, (new_cost, neighbor))
        return self._build_path(previous, start, end)
