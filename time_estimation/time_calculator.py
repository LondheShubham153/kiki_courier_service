from packages import Package
from vehicles import Vehicle
import pprint

class TimeCalculator:
    def __init__(self, base_del_cost,no_of_packges, no_of_vehicles,max_speed,max_carriable_weight):
        self.base_del_cost = base_del_cost
        self.no_of_packges = no_of_packges
        self.no_of_vehicles = no_of_vehicles
        self.max_carriable_weight = max_carriable_weight
        self.max_speed = max_speed
        self.packages = []
        self.vehicles = []

    def create_packages(self,pkg_ids,distances_in_km,pkg_weights_in_kg,offer_codes):
        for i in range(self.no_of_packges):
            self.packages.append(Package(pkg_ids[i],distances_in_km[i],pkg_weights_in_kg[i],offer_codes[i]))
    
    def create_vehicles(self,vehicle_ids,vehicle_speeds,vehicle_weights):
        for i in range(self.no_of_vehicles):
            self.vehicles.append(Vehicle(vehicle_ids[i],vehicle_speeds[i],vehicle_weights[i]))

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




if __name__ == "__main__":
    base_delivery_cost = 100
    no_of_packges = 5
    pkg_ids = ["PKG1","PKG2","PKG3","PKG4","PKG5"] 
    pkg_weights_in_kg = [50,75,175,110,155]
    distances_in_km = [30,125,100,60,95]
    offer_codes = ["OFFR01","OFFR02","OFFR03","OFFR04","OFFR05"]
    no_of_vehicles = 2
    max_speed = 70
    max_carriable_weight = 200

    veh_ids = ["VEH1","VEH2"]
    veh_speeds = [70,70]
    veh_max_weights = [200,200]

    time_calculator = TimeCalculator(base_delivery_cost,no_of_packges,no_of_vehicles,max_speed,max_carriable_weight)
    time_calculator.create_packages(pkg_ids,distances_in_km,pkg_weights_in_kg,offer_codes)
    
    time_calculator.create_vehicles(veh_ids,veh_speeds,veh_max_weights)
    pprint.pprint(time_calculator.calculate_delivery_time(time_calculator.packages))
    # time_calculator.calculate_delivery_time(time_calculator.packages)