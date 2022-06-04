"""
Created on 03/06/2022

@author: Shubham Londhe

A basic implementation of a click CLI app for the Kiki Courier Service.

"""
from time_estimation.time_calculator import TimeCalculator

from tabulate import tabulate
import click


@click.command()
@click.argument('base_delivery_cost', default=100)
@click.argument('no_of_packges', default=5)
def time_calculation(base_delivery_cost,no_of_packges):
    click.echo(f'Base Delivery Cost: {base_delivery_cost}')
    click.echo(f'No. of packges: {no_of_packges}')

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


if __name__ == '__main__':
    time_calculation()