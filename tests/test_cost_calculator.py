from offer_criteria.cost_calculator import CostCalculator
from offer_criteria.offers import Offer


def test_with_no_discount():
   cost_calculator = CostCalculator(100, 5, 5, "OFR001")
   assert cost_calculator.get_total_cost() == 175


def test_with_discount():
   cost_calculator = CostCalculator(100, 10, 100, "OFR003")
   assert cost_calculator.get_total_cost() == 665


def test_get_offer_discount():
   cost_calculator = CostCalculator(100, 10, 100, "OFR003")
   assert cost_calculator.get_offer_discount() == 0.05


def test_check_discount_conditions():
   cost_calculator = CostCalculator(100, 10, 100, "OFR003")
   offer = Offer("OFR003", 250,50,150,10,0.05,False)
   assert cost_calculator.check_discount_conditions(offer) == True


def test_calculate_delivery_cost():
   cost_calculator = CostCalculator(100, 10, 100, "OFR003")
   assert cost_calculator.calculate_delivery_cost() == 700


def test_get_applied_discount():
   cost_calculator = CostCalculator(100, 10, 100, "OFR003")
   assert cost_calculator.get_applied_discount() == 35.0

