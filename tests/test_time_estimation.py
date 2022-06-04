from time_estimation.time_calculator import TimeCalculator
import pytest

@pytest.fixture()
def time_calculator():
   return TimeCalculator(100,2,2,70,200)

@pytest.fixture()
def vehicles(time_calculator):
   return time_calculator.create_packages(["PKG1","PKG2"],[30,125],[50,75],["OFFR001","OFFR0008"])

@pytest.fixture()
def packages(time_calculator):
   return time_calculator.create_vehicles(["VEH1","VEH2"],[70,70],[200,200])


def test_delivery_times(time_calculator,packages,vehicles):
   final_packages = time_calculator.calculate_delivery_time(time_calculator.packages)
   assert final_packages[0].pkg_delivery_time == 1.79
   assert final_packages[1].pkg_delivery_time == 0.43


def test_get_max_weighted_package(time_calculator,packages,vehicles):
   final_packages = time_calculator.calculate_delivery_time(time_calculator.packages)
   assert time_calculator.get_max_weighted_package([final_packages]) == 75


def test_if_package_delivered(time_calculator,packages,vehicles):
   final_packages = time_calculator.calculate_delivery_time(time_calculator.packages)
   assert final_packages[0].pkg_delivered == True
   assert final_packages[1].pkg_delivered == True


def test_get_total_weight(time_calculator,packages,vehicles):
   assert time_calculator.get_total_weight(time_calculator.packages[0]) == 50