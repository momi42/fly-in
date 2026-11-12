from simulation.occupancy_manager import OccupancyManager


class Simulator:
    def _all_delivered(
            self,
            drones,
        ):
            return all(
                drone.delivered
                for drone in drones
            )

    def _build_occupancy(
        self,
        drones,
        occupancy,
    ):

        occupancy.reset()
        for drone in drones:
            if not drone.delivered:
                occupancy.register(
                    drone.current_zone
                )

    def _move_drone(
        self,
        drone,
        path,
        graph,
        occupancy,
    ):
        pass

    def simulate(
            self,
            drones,
            path,
            graph,
    ):
        occupancy = OccupancyManager()
        results = []
        while not self._all_delivered(drones):
            self._build_occupancy(drones, occupancy)
            turn_moves = []
            for drone in drones:
                move = self._move_drone(
                    drone,
                    path,
                    graph,
                    occupancy,
                )
                if move:
                    turn_moves.append(move)
            if  turn_moves:
                results.append(" ".join(turn_moves))
        return results
            



            #     if drone.delivered:
            #         continue
            #     next_zone_name = path[
            #         drone.path_index + 1
            #         ] if drone.path_index + 1 < len(path) else None
            #     next_zone = graph.zones.get(
            #         next_zone_name) if next_zone_name else None
            #     if occupancy.can_enter(next_zone):
            #         drone.path_index += 1
            #         zone = path[drone.path_index]
            #         occupancy.register(zone)
            #         turn_moves.append(f"D{drone.drone_id}-{zone}")
            #         occupancy.remove(drone.current_zone)
            #         drone.current_zone = zone
            #     if (drone.path_index == len(path) - 1):
            #         drone.delivered = True
            # if turn_moves:
            #     print(" ".join(turn_moves))

        
        # return turn_moves

        # movements = []
        # for zone in path[1:]:
        #     drone.current_zone = zone
        #     movements.append(f"D{drone.drone_id}-{zone}")
        # drone.delivered = True
        # return movements
