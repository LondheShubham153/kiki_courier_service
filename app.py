"""
Created on 03/06/2022

@author: Shubham Londhe

An Implementation of a CLI app for the Kiki Courier Service.

"""

from offer_criteria.cost_calculator import CostCalculator
from time_estimation.time_calculator import TimeCalculator
from tabulate import tabulate

while True:  
    print("\nWelcome to Kiki's Courier Service")  
    print("1. Calculate Offer Criteria")  
    print("2. Calculate Estimated Time for your Package")  
    print("3. Exit\n")  
    choice1 = int(input("Enter the Choice:\n"))  
  
    if choice1 == 1:  
        """
        This choice demonstrate user input for the following parameters:
        - Base Delivery Cost
        - Number of Packages
        - Max Speed
        - Package IDs
        - Package Distances
        - Package Weights
        - Offer Codes
        """
        pkg_weights = []
        pkg_ids = []
        pkg_distances = []
        pkg_offer_codes = []

        base_price = float(input("Enter the base price: "))
        no_of_packges = int(input("Enter the number of packages: "))

        for package in range(no_of_packges):
            pkg_id = input("Enter the package id: ")
            pkg_weight = int(input("Enter the package weight: "))
            pkg_distance = int(input("Enter the distance to destination: "))
            pkg_offer = input("Enter the offer code: ")
            pkg_ids.append(pkg_id)
            pkg_weights.append(pkg_weight)
            pkg_distances.append(pkg_distance)
            pkg_offer_codes.append(pkg_offer)
            cost_calculator = CostCalculator(base_price, pkg_weight, pkg_distance, pkg_offer)
        
        time_calculator = TimeCalculator(base_price,no_of_packges)
        time_calculator.create_packages(pkg_ids,pkg_distances,pkg_weights,pkg_offer_codes)
        final_packages = time_calculator.get_discounted_price(time_calculator.packages)
        headers = ["Package", "Discount", "Total Cost", "Total Time"]
        print(tabulate(final_packages, headers=headers))

    elif choice1 == 2:  
        """
        This choice demonstrates the pre loaded inputs for Time calculation
        """
        
        base_delivery_cost = 100
        no_of_packges = 5
        pkg_ids = ["PKG1","PKG2","PKG3","PKG4","PKG5"] 
        pkg_weights_in_kg = [50,75,175,110,155]
        distances_in_km = [30,125,100,60,95]
        offer_codes = ["OFFR01","OFFR02","OFFR03","OFR002","OFFR05"]
        no_of_vehicles = 2
        max_speed = 70
        max_carriable_weight = 200

        veh_ids = ["VEH1","VEH2"]
        veh_speeds = [70,70]
        veh_max_weights = [200,200]

        time_calculator = TimeCalculator(base_delivery_cost,no_of_packges,no_of_vehicles,max_speed,max_carriable_weight)
        time_calculator.create_packages(pkg_ids,distances_in_km,pkg_weights_in_kg,offer_codes)
        time_calculator.create_vehicles(veh_ids,veh_speeds,veh_max_weights)
        time_calculator.calculate_delivery_time(time_calculator.packages)

        final_packages = time_calculator.get_discounted_price(time_calculator.packages)
        headers = ["Package", "Discount", "Total Cost", "Total Time"]
        print(tabulate(final_packages, headers=headers))
    elif choice1 == 3:  
        print("See You Soon, Bye!")
        break  
      
    else:  
        print("Oops! Incorrect Choice.")  


