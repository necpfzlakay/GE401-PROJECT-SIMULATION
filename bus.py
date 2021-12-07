import random


class bus:
    print("bus")
    bus_value = 350000  # usd peace of bus
    bus_spended_energy = 0.85  # watt for one hour
    bus_total_number = 900  # total number of bus
    bus_passenger_num = 20
    bus_road_distance = 420 / 24

    # parameterized constructor
    def __init__(self):
        self.bus_value = 350000  # usd peace of bus
        self.bus_spended_energy = 0.85  # watt for one KM
        self.bus_road_distance = 500 / 24
        self.bus_total_number = 900  # total number of bus
        self.bus_passenger_num = 20

    def getSpendedEnergy(self):
        # return self.bus_spended_energy
        return random.uniform(0.7, 0.99)

    def getBusPassengerNum(self):
        # return self.bus_passenger_num
        return random.randint(15, 50)

    def getTotalBusNum(self):
        return self.bus_total_number

    def getRoadDistance(self):
        # return self.bus_road_distance
        return random.uniform(380/24, 470/24)
