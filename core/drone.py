from dataclasses import dataclass


@dataclass
class Drone:
    drone_id: int
    current_zone: str
    delivered: bool = False
