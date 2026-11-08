from dataclasses import dataclass


@dataclass
class Zone:
    name: str
    x: int
    y: int
    zone_type: str = "normal"
    max_drones: int = 1

    def cost(self):
        if self.zone_type == "restricted":
            return 2
        if self.zone_type == "blocked":
            return float("inf")
        return 1
