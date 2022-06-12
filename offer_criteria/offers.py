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

    def _create_offers_map(self):
        offers_map = {}
        for offer in self.offers:
            offers_map[offer.code] = offer
        return offers_map
    
    def _create_offer(self,code,max_dist,min_dist,max_weight,min_weight,discount):
        offers = []
        return offers.append(Offer(code,max_dist,min_dist,max_weight,min_weight,discount))

