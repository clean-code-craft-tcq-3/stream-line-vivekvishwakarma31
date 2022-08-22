from receiver import *
import unittest


class senderTest(unittest.TestCase):
    def test_update_temperature(self):
        receiver = Recevier()
        receiver.updateTemperatureValues(50)
        receiver.updateTemperatureValues(20)
        receiver.updateTemperatureValues(50)
        receiver.updateTemperatureValues(70)
        self.assertTrue(receiver.max_temperature == 70)
        self.assertTrue(receiver.min_temperature == 20)
        receiver.updateTemperatureValues(180)
        receiver.updateTemperatureValues(220)
        receiver.updateTemperatureValues(120)
        receiver.updateTemperatureValues(-20)
        self.assertTrue(receiver.max_temperature == 220)
        self.assertTrue(receiver.min_temperature == -20)

    def test_update_charge(self):
        receiver = Recevier()
        receiver.updateChargeValues(70)
        receiver.updateChargeValues(40)
        receiver.updateChargeValues(20)
        receiver.updateChargeValues(35)
        receiver.updateChargeValues(125)
        receiver.updateChargeValues(139)
        receiver.updateChargeValues(23)
        self.assertTrue(receiver.max_charge == 139)
        self.assertTrue(receiver.min_charge == 20)

    def test_update_moving_avg(self):
        receiver = Recevier()
        receiver.computeMovingAvg(30, 40)
        receiver.computeMovingAvg(20, 20)
        receiver.computeMovingAvg(50, 30)
        receiver.computeMovingAvg(40, 60)
        receiver.computeMovingAvg(70, 70)
        self.assertTrue(receiver.last_five_temp_array == [30, 20, 50, 40, 70])
        self.assertTrue(receiver.last_five_charge_array ==
                        [40, 20, 30, 60, 70])
        self.assertTrue(receiver.moving_average_temp == 42)
        self.assertTrue(receiver.moving_average_charge == 44)
        receiver.computeMovingAvg(25, 30)
        receiver.computeMovingAvg(34, 15)
        receiver.computeMovingAvg(25, 35)
        self.assertTrue(receiver.last_five_temp_array == [40, 70, 25, 34, 25])
        self.assertTrue(receiver.last_five_charge_array ==
                        [60, 70, 30, 15, 35])
        self.assertTrue(receiver.moving_average_temp == 38.8)
        self.assertTrue(receiver.moving_average_charge == 42)


if __name__ == '__main__':
    unittest.main()
