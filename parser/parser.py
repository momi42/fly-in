from core.map_data import MapData
from core.zone import Zone


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
            if line.startswith('start_hub'):
                map_data.start_hub= line.split(":")[1].split()[0]
            if line.startswith('end_hub'):
                map_data.end_hub = line.split(":")[1].split()[0]
            if line.startswith('hub'):
                name , x, y, meta = line.split(":")[1].split()
                zone = Zone(name, int(x), int(y))
                map_data.zones.append(zone)
        return(map_data)