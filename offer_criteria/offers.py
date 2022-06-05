"""
Created on 29/05/2022

@author: Shubham Londhe

Data Class Implementation for offers that can be extended 
to any new Offers to be added.

"""

from dataclasses import dataclass

@dataclass
class Offer:
    code: str
    max_dist: int
    min_dist: int
    max_weight: int
    min_weight: int
    discount: float
    is_used: bool = False

    def _create_offers(self,codes,max_distances,min_distances,max_weights,min_weights,discounts):
        for i in range(self.no_of_offers):
            self.offers.append(Offer(codes[i],max_distances[i],min_distances[i],max_weights[i],min_weights[i],discounts[i]))

# Some Sample Offers
offer_1 = Offer("OFR001", 200,0,200,70,0.01,False)
offer_2 = Offer("OFR002", 150,50,250,100,0.07,False)
offer_3 = Offer("OFR003", 250,50,150,10,0.05,False)
