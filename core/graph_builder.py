from core.graph import Graph
from core.map_data import MapData
from core.zone import Zone


class GraphBuilder:

    def build(self, map_data: MapData):

        graph = Graph()
        start_zone = Zone(map_data.start_hub, 0, 0,)
        end_zone = Zone(map_data.end_hub, 0, 0,)
        graph.add_zone(start_zone)
        graph.add_zone(end_zone)
        for zone in map_data.zones:
            graph.add_zone(zone)

        print(graph.adjacency)
        
        for connection in map_data.connections:
            graph.add_connection(
                connection.start,
                connection.end,
            )

        return graph