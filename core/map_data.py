from dataclasses import dataclass, field


@dataclass
class MapData:
    drone_count: int = 0
    start_hub: str = ""
    end_hub: str = ""
    zones: list = field(default_factory=list)
    connections: list = field(default_factory=list)
