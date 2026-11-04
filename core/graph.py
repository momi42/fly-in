class Graph:

    def __init__(self):
        self.zones = {}
        self.adjacency = {}

    def add_zone(self, zone):
        self.zones[zone.name] = zone
        if zone.name not in self.adjacency:
            self.adjacency[zone.name] = []

    def add_connection(self, start, end):
        if start not in self.adjacency:
            raise ValueError(f"Unknown zone: {start}")
        if end not in self.adjacency:
            raise ValueError(f"Unknown zone: {end}")
        self.adjacency[start].append(end)
        self.adjacency[end].append(start)

    def neighbors(self, zone_name):
        return self.adjacency[zone_name]