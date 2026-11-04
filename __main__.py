from core.zone import Zone
from core.connection import Connection
from core.graph import Graph
from parser.parser import Parser
from parser.exceptions import ParserError

# =====Test per parser======
parser = Parser()
try:
    data = parser.parse("maps/easy/01_linear_path.txt")
    print(data)
except ParserError as e:
    print(f"\033[31m {e} \033[0m")


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