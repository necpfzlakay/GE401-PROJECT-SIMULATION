import random


class Battery:
    battery_number = 100
    battery_price = 756  # one peace of usd
    battery_capacity = 10  # Kwatt in one hour avg

    # parameterized constructor
    def __init__(self):
        # self.battery_number = 10
        self.battery_number = 21351
        self.battery_price = 1500  # one peace of usd
        self.battery_capacity = 10  # Kwatt totatll

    print("battery")

    def getBatteryCapacity(self):
        return self.battery_capacity

    def getBatteryNum(self):
        return self.battery_number

    def increaseBatteryNum(self):
        self.battery_number += 10
