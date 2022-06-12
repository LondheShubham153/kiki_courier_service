"""
Created on 02/06/2022

@author: Shubham Londhe

Data Class Implementation for Vehicles that can be extended 
to any new Vehicles to be added.

"""
from dataclasses import dataclass

@dataclass
class Vehicle:
    vehicle_id: int
    max_speed: int = 70
    max_weight: int = 200
    hours : float = 0.0
    is_available: bool = True

    def _create_vehicles(self,no_of_vehicles,vehicle_ids,vehicle_speeds,vehicle_weights):
        vehicles = []
        for i in range(no_of_vehicles):
            vehicles.append(Vehicle(vehicle_ids[i],vehicle_speeds[i],vehicle_weights[i]))
        return vehicles

    def _get_current_vehicle(vehicle_on_trip):
        """
        Returns the current vehicle on trip
        based on the vehicle on trip list availability
        """
        if not vehicle_on_trip:
            return None
        vehicle_available = None
        for vehicle in vehicle_on_trip:
            if not vehicle_available:
                vehicle_available = vehicle
                continue
            if vehicle_available.hours > vehicle.hours:
                vehicle_available = vehicle
        return vehicle_available
