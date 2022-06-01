from dataclasses import dataclass

@dataclass
class Package:
    pkg_id: str
    pkg_dist: int
    pkg_weight: int
    pkg_offer: str
    pkg_delivered: bool = False
    pkg_delivery_time: float = 0.0
    
    def __post_init__(self):
        self.sort_index = self.pkg_weight

pkg_1 = Package("PKG1", 30,50,"OFFR001")
