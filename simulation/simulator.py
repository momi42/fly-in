class Simulator:
    def simulate(
            self,
            drones,
            path,
    ):
        while True:
            if all(drone.delivered for drone in drones):
                break
            turn_moves = []
            for drone in drones:
                if drone.delivered:
                    continue
                drone.path_index += 1
                zone = path[drone.path_index]
                turn_moves.append(f"D{drone.drone_id}-{zone}")
                if (drone.path_index == len(path) - 1):
                    drone.delivered = True
            if turn_moves:
                print(" ".join(turn_moves))
        # return turn_moves


        # movements = []
        # for zone in path[1:]:
        #     drone.current_zone = zone
        #     movements.append(f"D{drone.drone_id}-{zone}")
        # drone.delivered = True
        # return movements

