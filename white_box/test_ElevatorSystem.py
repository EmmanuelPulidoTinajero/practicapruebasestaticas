import unittest
from class_exercises import ElevatorSystem

class TestElevatorSystem(unittest.TestCase):
    def setUp(self):
        self.MyElevator = ElevatorSystem()

    def test___init__(self):
        self.assertEqual(self.MyElevator.state, "Idle")

    def test_move_up(self):
        self.MyElevator.state = "Idle"
        self.assertEqual(self.MyElevator.move_up(), "Elevator moving up")
        self.assertEqual(self.MyElevator.state, "Moving Up")

    def test_move_upstatenotidle(self):
        self.MyElevator.state = "otra"
        self.assertEqual(self.MyElevator.move_up(), "Invalid operation in current stateup")

    def test_move_down(self):
        self.MyElevator.state = "Idle"
        self.assertEqual(self.MyElevator.move_down(), "Elevator moving down")
        self.assertEqual(self.MyElevator.state, "Moving Down")

    def test_move_downstatenotidle(self):
        self.MyElevator.state = "otra"
        self.assertEqual(self.MyElevator.move_down(), "Invalid operation in current state")

    def test_stopMoving_Up(self):
        self.MyElevator.state = "Moving Up"
        self.assertEqual(self.MyElevator.stop(), "Elevator stopped")
        self.assertEqual(self.MyElevator.state, "Idle")

    def test_stopMoving_Down(self):
        self.MyElevator.state = "Moving Down"
        self.assertEqual(self.MyElevator.stop(), "Elevator stopped")
        self.assertEqual(self.MyElevator.state, "Idle")
    def test_stopMoving(self):
        self.MyElevator.state = "otro"
        self.assertEqual(self.MyElevator.stop(), "Invalid operation in current state")
        


