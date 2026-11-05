class Simulator:
    def simulate(
            self,
            drone,
            path,
    ):
        movements = []
        for zone in path[1:]:
            drone.current_zone = zone
            movements.append(f"D{drone.drone_id}-{zone}")
        drone.delivered = True
        return movements
