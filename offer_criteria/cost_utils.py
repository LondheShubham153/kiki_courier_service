from .offers import Offer

class CostUtils:
    def __init__(self):
        self.offers = []
        self.create_offers_map()

    def create_offers_map(self):
        self.offers_map = Offer._create_offers_map(self)


    def check_discount_conditions(self,offer):
        if offer.max_weight >= self.weight >= offer.min_weight:
            if offer.max_dist >= self.distance >= offer.min_dist:
                return True
        return False


    def get_offer_discount(self):
        offer = self.offers_map.get(self.offer_code)
        if offer:
            if self.check_discount_conditions(offer) and not offer.is_used:
                return offer.discount
        return 0

    def calculate_delivery_cost(self):
        return self.base_del_cost + (self.weight * 10) + (self.distance * 5)
        
    def get_applied_discount(self):
        return round(self.calculate_delivery_cost() * self.get_offer_discount(),2)
    
    def get_total_cost(self):
        return self.calculate_delivery_cost() - self.get_applied_discount()
