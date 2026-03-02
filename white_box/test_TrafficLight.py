import unittest
from class_exercises import TrafficLight
class TestTrafficLight(unittest.TestCase):
    def setUp(self):
        self.myTrafficLight = TrafficLight()

    def test_Init(self):
        self.assertEqual(self.myTrafficLight.state,  "Red")

    def test_change_state_red(self):
        self.myTrafficLight.state = "Red"
        self.myTrafficLight.change_state()
        self.assertEqual(self.myTrafficLight.state, "Green")

    def test_change_state_green(self):
        self.myTrafficLight.state = "Green"
        self.myTrafficLight.change_state()
        self.assertEqual(self.myTrafficLight.state, "Yellow")

    def test_change_state_yellow(self):
        self.myTrafficLight.state = "Yellow"
        self.myTrafficLight.change_state()
        self.assertEqual(self.myTrafficLight.state,  "Red")

    def test_get_current_state(self):
        self.assertEqual(self.myTrafficLight.get_current_state(), self.myTrafficLight.state)