from core.map_data import MapData
from core.zone import Zone
from core.connection import Connection


class Parser:

    def parse(self, file_path: str):
        with open(file_path, "r") as file:
            lines = file.readlines()

        map_data = MapData()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue
            if line.startswith('nb_drones'):
                map_data.drone_count = int(line.split(":")[1])
            elif line.startswith('start_hub'):
                map_data.start_hub= line.split(":")[1].split()[0]
            elif line.startswith('end_hub'):
                map_data.end_hub = line.split(":")[1].split()[0]
            elif line.startswith('hub'):
                name , x, y = line.split(":")[1].split()[:3]
                zone = Zone(name, int(x), int(y))
                map_data.zones.append(zone)
            elif line.startswith('connection'):
                connection_data = line.split(":")[1].strip
                start , end = connection_data.split("-")
                connection = Connection(start, end)
                map_data.connections.append(connection)
        return(map_data)