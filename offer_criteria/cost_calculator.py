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


    def get_offer_discount(self):
        """
        Get the discount for the offer code
        """
        offer = self.offers_map.get(self.offer_code)
        if offer:
            if self.check_discount_conditions(offer) and not offer.is_used:
                offer.is_used = True
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
        return self.calculate_delivery_cost() * self.get_offer_discount()
    
    def get_total_cost(self):
        """
        Get the total cost
        """
        return self.calculate_delivery_cost() - self.get_applied_discount()

if __name__ == "__main__":
    base_price = float(input("Enter the base price: "))
    packages = int(input("Enter the number of packages: "))

    for package in range(packages):
        pkg_weight = int(input("Enter the package weight: "))
        pkg_distance = int(input("Enter the distance to destination: "))
        pkg_name = input("Enter the package name: ")
        pkg_offer = input("Enter the offer code: ")

        cost_calculator = CostCalculator(base_price, pkg_weight, pkg_distance, pkg_offer)
        print(f"{pkg_name} {cost_calculator.get_applied_discount()}, {cost_calculator.get_total_cost()}")

    
