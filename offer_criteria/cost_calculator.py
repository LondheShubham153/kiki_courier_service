"""
Created on 29/05/2022

@author: Shubham Londhe

Implementation of Problem 1 of the Kiki Courier Service that does
the cost calculation based on the offers Provided.

"""

from .offers import offer_1,offer_2,offer_3

class CostCalculator:
    def __init__(self, base_del_cost, weight,distance, offer_code):
        self.base_del_cost = base_del_cost
        self.weight = weight
        self.distance = distance
        self.offer_code = offer_code
        self.create_offers_map()

    def create_offers_map(self):
        self.offers_map = {
            offer_1.code: offer_1,
            offer_2.code: offer_2,
            offer_3.code: offer_3
        }


    def check_discount_conditions(self,offer):
        """
        Check if the offer conditions are met
        """
        if offer.max_weight >= self.weight >= offer.min_weight:
            if offer.max_dist >= self.distance >= offer.min_dist:
                return True
        return False


    def get_offer_discount(self,offer_code=None):
        """
        Get the discount for the offer code
        """
        offer = self.offers_map.get(self.offer_code)
        if offer:
            if self.check_discount_conditions(offer) and not offer.is_used:
                return offer.discount
        return 0

    def calculate_delivery_cost(self):
        """
        Base Delivery Cost + (Package Total Weight * 10) +
        (Distance to Destination * 5)
        """
        return self.base_del_cost + (self.weight * 10) + (self.distance * 5)
        
    def get_applied_discount(self):
        """
        Apply the offer discount
        """
        return round(self.calculate_delivery_cost() * self.get_offer_discount(),2)
    
    def get_total_cost(self):
        """
        Get the total cost
        """
        return self.calculate_delivery_cost() - self.get_applied_discount()
