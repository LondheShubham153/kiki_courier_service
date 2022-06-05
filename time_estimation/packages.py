"""
Created on 29/05/2022

@author: Shubham Londhe

Data Class Implementation for Packages that can be extended 
to any new Packages to be added.

"""

from dataclasses import dataclass

@dataclass
class Package:
    pkg_id: str
    pkg_dist: int
    pkg_weight: int
    pkg_offer: str
    pkg_delivered: bool = False
    pkg_delivery_time: float = 0.0
    pkg_discount : float = 0.0
    pkg_total_cost : float = 0.0
    
    def __post_init__(self):
        self.sort_index = self.pkg_weight

    def _create_packages(self,pkg_ids,distances_in_km,pkg_weights_in_kg,offer_codes):
        for i in range(self.no_of_packges):
            self.packages.append(Package(pkg_ids[i],distances_in_km[i],pkg_weights_in_kg[i],offer_codes[i]))
    
    def _show_packages(self,packages):
        pkg_ids = [package.pkg_id for package in packages]
        pkg_discounts = [package.pkg_discount for package in packages]
        pkg_total_costs = [package.pkg_total_cost for package in packages]
        pkg_pkg_delivery_time = [package.pkg_delivery_time for package in packages]
        return{
            "pkg_ids":pkg_ids,
            "pkg_discounts":pkg_discounts,
            "pkg_total_costs":pkg_total_costs,
            "pkg_delivery_time":pkg_pkg_delivery_time
        }

# Spme Sample Packages
pkg_1 = Package("PKG1", 30,50,"OFFR001")
pkg_2 = Package("PKG2", 130,250,"OFFR002")
pkg_3 = Package("PKG3", 90,150,"OFFR003")
