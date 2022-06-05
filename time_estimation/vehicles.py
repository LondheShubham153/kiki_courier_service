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

    def _create_vehicles(self,vehicle_ids,vehicle_speeds,vehicle_weights):
        for i in range(self.no_of_vehicles):
            self.vehicles.append(Vehicle(vehicle_ids[i],vehicle_speeds[i],vehicle_weights[i]))
    
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

# Some Sample Vehicles
veh_1 = Vehicle("VH1", 70,200,True)
veh_2 = Vehicle("VH2", 70,200,True)
