from dataclasses import dataclass

@dataclass
class Offer:
    code: str
    max_dist: int
    min_dist: int
    max_weight: int
    min_weight: int
    discount: float
    is_used: bool


offer_1 = Offer("OFR001", 200,0,200,70,0.01,False)
offer_2 = Offer("OFR002", 150,50,250,100,0.07,False)
offer_3 = Offer("OFR003", 250,50,150,10,0.05,False)
