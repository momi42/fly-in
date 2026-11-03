from core.zone import Zone
from core.connection import Connection
from core.graph import Graph


graph = Graph()

zone_a = Zone("A", 0, 0)
zone_b = Zone("B", 1, 1)
zone_c = Zone("C", 2, 2)

connection = Connection("A", "B")
connection2 = Connection("B", "C")

graph.zones["A"] = zone_a
graph.zones["B"] = zone_b
graph.zones["C"] = zone_c

graph.connections.append(connection)
graph.connections.append(connection2)

print(graph.zones)
print(graph.connections)