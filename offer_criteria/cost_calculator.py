"""
Created on 29/05/2022

@author: Shubham Londhe

Implementation of Problem 1 of the Kiki Courier Service that does
the cost calculation based on the offers Provided.

"""


from offer_criteria.cost_utils import CostUtils


class CostCalculator(CostUtils):
    def __init__(self, base_del_cost, weight,distance, offer_code):
        self.base_del_cost = base_del_cost
        self.weight = weight
        self.distance = distance
        self.offer_code = offer_code
        super().__init__()
    
    def get_discounted_price(self):
        return self.calculate_delivery_cost() - self.get_applied_discount()
        