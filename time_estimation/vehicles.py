from dataclasses import dataclass

@dataclass
class Vehicle:
    vehicle_id: int
    max_speed: int
    max_weight: int
    hours : float = 0.0
    is_available: bool = True

    def _get_current_vehicle(vehicle_on_trip):
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

veh_1 = Vehicle("VH1", 70,200,True)
veh_2 = Vehicle("VH2", 70,200,True)
