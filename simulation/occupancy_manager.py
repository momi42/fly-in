class OccupancyManager:
    def __init__(self):
        self.occupancy = {}

    def reset(self):
        self.occupancy = {}

    def register(
        self,
        zone_name,
    ):
        if zone_name not in self.occupancy:
            self.occupancy[zone_name] = 0
        self.occupancy[zone_name] += 1

    def remove(
            self,
            zone_name,
    ):
        if zone_name in self.occupancy:
            self.occupancy[zone_name] -= 1

    def can_enter(
            self,
            zone,
    ):
        return (self.occupancy.get(zone.name, 0) < zone.max_drones)
