"""
Created on 01/06/2022

@author: Shubham Londhe

Implementation of Problem 2 of the Kiki Courier Service that does
the Time Estimation based on the Package Details Provided.

"""

from offer_criteria.cost_calculator import CostCalculator
from time_estimation.time_utils import TimeUtils

class TimeCalculator(TimeUtils):
    def __init__(self, base_del_cost,no_of_packges, no_of_vehicles=2,max_speed=70,max_carriable_weight=200):
        self.base_del_cost = base_del_cost
        self.no_of_packges = no_of_packges
        self.no_of_vehicles = no_of_vehicles
        self.max_carriable_weight = max_carriable_weight
        self.max_speed = max_speed
        self.packages = []
        self.vehicles = []
        super().__init__()

    def calculate_delivery_time(self,packages_group):
        delivered_packages = []
        current_vehicle = self.vehicles[0]

        while len(delivered_packages) < len(self.packages):
            current_trip_time = []
            current_packages = self.dispatch_packages(packages_group)
            for package in current_packages:
                package.pkg_delivered = True
                trip_time = round(package.pkg_dist / float(self.max_speed),2)
                package.pkg_delivery_time = current_vehicle.hours + trip_time
                current_trip_time.append(trip_time)
                delivered_packages.append(package)
            current_vehicle.hours = max(current_trip_time) * 2
            current_vehicle = self.allocate_vehicle()
        return delivered_packages

    def get_discounted_price(self,packages):
        for package in packages:
            cost_calculator = CostCalculator(self.base_del_cost,
                                            package.pkg_weight,
                                            package.pkg_dist,
                                            package.pkg_offer
                                        )
            package.pkg_discount = cost_calculator.get_applied_discount()
            package.pkg_total_cost = cost_calculator.get_total_cost() - cost_calculator.get_applied_discount()
        return self.show_final_packages() 

    