import random
# 900 otobüs 0.85 -> 370000 watt


class solar_system:
    panel_number = 100
    panel_value = 1500  # one peace of usd
    panel_earning_energy = 0.6  # watt in one hour avg

    # parameterized constructor
    def __init__(self):
        # self.panel_number = 100
        self.panel_number = 61666
        self.panel_value = 1500
        # self.panel_earning_energy = 0.275
        self.panel_earning_energy = 0.6  # avg kw

    print("solar system")

    def getPanelNumber(self):
        return self.panel_number

    def getPanelEarningEnergy(self):

        # return self.panel_earning_energy
        return random.uniform(0.45, 0.7)

    def increasePanelNum(self):
        self.panel_number += 10
