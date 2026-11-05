from core.zone import Zone
from core.connection import Connection
from core.graph import Graph
from core.drone import Drone
from parser.parser import Parser
from parser.exceptions import ParserError
from core.graph_builder import GraphBuilder
from pathfinding.bfs import BFS
from pathfinding.dijkstra import Dijkstra
from simulation.simulator import Simulator


# =====Test per Dijkstra======
parser = Parser()
try:
    data = parser.parse("maps/easy/01_linear_path.txt")
    graph = GraphBuilder().build(data)
    path = Dijkstra().find_path(graph, data.start_hub, data.end_hub)
    drone = Drone(drone_id=1, current_zone=data.start_hub)
    movements = Simulator().simulate(drone, path)
    for m in movements:
        print(m)
except ParserError as e:
    print(f"\033[31m {e} \033[0m")


# # =====Test per BFS======
# parser = Parser()
# try:
#     data = parser.parse("maps/easy/01_linear_path.txt")
#     graph = GraphBuilder().build(data)
#     path = BFS().find_path(graph, "start", "goal")
#     print(path)
# except ParserError as e:
#     print(f"\033[31m {e} \033[0m")

# # =====Test per parser======
# parser = Parser()
# try:
#     data = parser.parse("maps/easy/01_linear_path.txt")
#     graph = GraphBuilder().build(data)
#     print(graph.adjacency)
# except ParserError as e:
#     print(f"\033[31m {e} \033[0m")


# =====Test per core======
# graph = Graph()

# zone_a = Zone("A", 0, 0)
# zone_b = Zone("B", 1, 1)
# zone_c = Zone("C", 2, 2)

# connection = Connection("A", "B")
# connection2 = Connection("B", "C")

# graph.zones["A"] = zone_a
# graph.zones["B"] = zone_b
# graph.zones["C"] = zone_c

# graph.connections.append(connection)
# graph.connections.append(connection2)

# print(graph.zones)
# print(graph.connections)
