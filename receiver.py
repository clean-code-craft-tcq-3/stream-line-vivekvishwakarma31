class Recevier:
    def __init__(self):
        self.min_temperature = 999
        self.max_temperature = 0
        self.min_charge = 999
        self.max_charge = 0
        self.last_five_temp_array = []
        self.last_five_charge_array = []
        self.moving_average_temp = 0
        self.moving_average_charge = 0

    def update_max_temperature(self, new_temp_value):
        if(new_temp_value > self.max_temperature):
            self.max_temperature = new_temp_value

    def update_min_temperature(self, new_temp_value):
        if(new_temp_value < self.max_temperature):
            self.min_temperature = new_temp_value

    def update_max_charge(self, new_charge_value):
        if(new_charge_value > self.max_charge):
            self.max_charge = new_charge_value

    def update_min_charge(self, new_charge_value):
        if(new_charge_value < self.min_charge):
            self.min_charge = new_charge_value

    def computeTemperatureMovingAvg(self, new_temp_value):
        if(len(self.last_five_temp_array) == 5):
            self.last_five_temp_array.pop(0)

        self.last_five_temp_array.append(new_temp_value)
        self.moving_average_temp = sum(
            self.last_five_temp_array)/(len(self.last_five_temp_array))

    def computeChargeMovingAvg(self, new_charge_value):
        if(len(self.last_five_charge_array) == 5):
            self.last_five_charge_array.pop(0)

        self.last_five_charge_array.append(new_charge_value)
        self.moving_average_charge = sum(
            self.last_five_charge_array)/(len(self.last_five_charge_array))

    def computeMovingAvg(self, new_temp_value, new_charge_value):
        self.computeTemperatureMovingAvg(new_temp_value)
        self.computeChargeMovingAvg(new_charge_value)

    def updateTemperatureValues(self, new_temp_value):
        self.update_max_temperature(new_temp_value)
        self.update_min_temperature(new_temp_value)

    def updateChargeValues(self, new_charge_value):
        self.update_max_charge(new_charge_value)
        self.update_min_charge(new_charge_value)

    def computeMinMaxAvgSensorValues(self, new_temp_value, new_charge_value):
        self.updateTemperatureValues(new_temp_value)
        self.updateChargeValues(new_charge_value)
        self.computeMovingAvg(new_temp_value, new_charge_value)

    def handleInput(self, string_input):
        # Temperature : Value, Charge : Value
        sensor_data = string_input.split(",")
        sensor_data[0] = sensor_data[0].replace(" ", "")
        sensor_data[1] = sensor_data[1].replace(" ", "")

        temperature_data = sensor_data[0].split(":")
        new_temp_value = int(temperature_data[1])

        charge_data = sensor_data[1].split(":")
        new_charge_value = int(charge_data[1])

        self.computeMinMaxAvgSensorValues(new_temp_value, new_charge_value)

    def printDetails(self):
        print("Max Temperature", self.max_temperature)
        print("Min Temperature", self.min_temperature)
        print("Max Charge", self.max_charge)
        print("Min Charge", self.min_charge)
        print("Moving Avg Temperature", self.moving_average_temp)
        print("Moving Avg Charge", self.moving_average_charge)


if __name__ == "__main__":
    recieiver = Recevier()
    print("Reciever Started")
    while True:
        try:
            input_line = input()
            print(input_line)
        except EOFError:
            break
    recieiver.printDetails()
