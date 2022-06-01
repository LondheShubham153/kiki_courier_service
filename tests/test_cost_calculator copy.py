from offer_criteria.cost_calculator import CostCalculator

def test_with_no_discount():
   cost_calculator = CostCalculator(100, 5, 5, "OFR001")
   assert cost_calculator.get_total_cost() == 175


def test_with_discount():
   cost_calculator = CostCalculator(100, 10, 100, "OFR003")
   assert cost_calculator.get_total_cost() == 665

def test_get_offer_discount():
   cost_calculator = CostCalculator(100, 10, 100, "OFR003")
   assert cost_calculator.get_offer_discount() == 0