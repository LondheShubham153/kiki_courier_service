from time_estimation.packages import Package
from time_estimation.vehicles import Vehicle
from offer_criteria.cost_calculator import CostCalculator

class TimeUtils:
        
    def create_packages(self,no_of_packges,pkg_ids,distances_in_km,pkg_weights_in_kg,offer_codes):
        self.packages = Package._create_packages(self,no_of_packges,pkg_ids,distances_in_km,pkg_weights_in_kg,offer_codes)


    def create_vehicles(self,no_of_vehicles,vehicle_ids,vehicle_speeds,vehicle_weights):
        self.vehicles = Vehicle._create_vehicles(self,no_of_vehicles,vehicle_ids,vehicle_speeds,vehicle_weights)


    def sort_packages(self):
        for i in range(self.no_of_packges):
            for j in range(self.no_of_packges):
                if self.packages[i].pkg_weight > self.packages[j].pkg_weight:
                    temp = self.packages[i]
                    self.packages[i] = self.packages[j]
                    self.packages[j] = temp
    

    def get_total_weight(self,package):
        total_weight = 0
        total_weight += package.pkg_weight
        return total_weight
    

    def get_max_weighted_package(self,packages):
        max_weight = 0
        if not packages:
            return max_weight

        for package in packages:
            if package:
                if package[0].pkg_weight > max_weight:
                    max_weight = package[0].pkg_weight
        return max_weight

    def allocate_vehicle(self):
        return Vehicle._get_current_vehicle(self.vehicles)

    def dispatch_packages(self,packages_group):
        packages_to_dispatch = {}
        package_in_transit = []
        package_index = 0
        total_weight = 0

        while package_index < len(packages_group) and total_weight < self.max_carriable_weight:
            for package in packages_group[package_index:]:
                if not package.pkg_delivered:
                    if total_weight + package.pkg_weight <= self.max_carriable_weight:
                        total_weight = self.get_total_weight(package)
                        package_in_transit.append(package)
            
            packages_to_dispatch[total_weight] = package_in_transit
            package_in_transit = []
            total_weight = 0
            package_index += 1
        return packages_to_dispatch[self.get_max_weighted_package(packages_to_dispatch.values())]

    
    
    def show_final_packages(self):
        return Package._show_packages(self,self.packages)