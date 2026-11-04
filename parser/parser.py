from core import map_data
from core.map_data import MapData
from core.zone import Zone
from core.connection import Connection
from parser.exceptions import ParserError


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
                if map_data.drone_count <= 0:
                    raise ParserError("Number of drones must be positiv")
            elif line.startswith('start_hub'):
                if map_data.start_hub:
                    raise ParserError("Multiple start hubs found")
                map_data.start_hub= line.split(":")[1].split()[0]
            elif line.startswith('end_hub'):
                if map_data.end_hub:
                    raise ParserError("Multiple end hubs found")
                map_data.end_hub = line.split(":")[1].split()[0]
            elif line.startswith('hub'):
                name , x, y = line.split(":")[1].split()[:3]
                new_zone = Zone(name, int(x), int(y))
                for existing_zone in map_data.zones:
                    if existing_zone.name == name:
                        raise ParserError(f"Duplicate zone: {name}")
                map_data.zones.append(new_zone)
            elif line.startswith('connection'):
                connection_data = line.split(":")[1].strip()
                start, end = connection_data.split("-")
                connection = Connection(start, end)
                map_data.connections.append(connection)

        if not map_data.start_hub:
            raise ParserError("Missing start_hub")
        if not map_data.end_hub:
            raise ParserError("Missing end_hub")
        return(map_data)