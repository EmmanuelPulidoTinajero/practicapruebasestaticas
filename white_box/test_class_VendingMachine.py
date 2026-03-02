import unittest
from class_exercises import VendingMachine

class TestVendingMachine(unittest.TestCase):
            
    def setUp(self):
        self.myVendingMachine  = VendingMachine()
        
    def test_init_VendingMachine(self):
        self.assertEqual(self.myVendingMachine.state, "Ready")

    def test_insert_coin_state_ready(self):
        self.assertEqual(self.myVendingMachine.insert_coin(), "Coin Inserted. Select your drink.")
        self.assertEqual(self.myVendingMachine.state, "Dispensing")
    def test_insert_coin_state_not_ready(self):
        self.myVendingMachine.state = "hola"
        self.assertEqual(self.myVendingMachine.insert_coin(), "Invalid operation in current state.")

    def test_select_drink(self):
        self.myVendingMachine.state = "Dispensing"
        self.assertEqual(self.myVendingMachine.select_drink(), "Drink Dispensed. Thank you!")

        def test_select_drink(self):
            self.myVendingMachine.state = "Ready"
            self.assertEqual(self.myVendingMachine.select_drink(), "Invalid operation...")