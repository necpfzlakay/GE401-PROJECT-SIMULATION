import bus
import solar_system
import battery
import random

panel = solar_system.solar_system()
battery = battery.Battery()
oneBus = bus.bus()
busList = []
for i in range(oneBus.getTotalBusNum()):
    busList.append(bus.bus())

energy_daily = 1
money_balance = 1
battery_balance = 1
battery_capacity = 1

lossList = [1, 0]

bus_spended_energy = 0
distance = 0
passanger = 0
year = 1
DAILY_PASSANGER = []
DAILY_DISTANCE = []
DAILY_GAINED_ENERGY = []
DAILY_SPENDED_ENERGY = []
TOTAL_GAINED_ENERGY = 1
TOTAL_SPENDED_ENERGY = 1
TOTAL_PASSANGER = 1
TOTAL_SPENDED_MONEY = 1
TOTAL_LOSS_PANEL = 0
TOTAL_LOSS_BUSS = 0
count = 0
for daysIndex in range(1, 365 * year): 

    battery_capacity = battery.getBatteryCapacity() * battery.getBatteryNum()
    print("capacity", battery_capacity)
    for hoursIndex in range(0, 24):
        for index in busList:
            bus_spended_energy += index.getSpendedEnergy() * index.getRoadDistance()
            TOTAL_PASSANGER += index.getBusPassengerNum()
            distance += index.getRoadDistance()
            passanger += index.getBusPassengerNum()
 
        TOTAL_SPENDED_ENERGY += bus_spended_energy
        if(21 > hoursIndex > 8):  # solar_panel_status = "on"
            energy_daily = panel.getPanelEarningEnergy() * panel.getPanelNumber()
   
            TOTAL_GAINED_ENERGY += panel.getPanelEarningEnergy() * panel.getPanelNumber()
            DAILY_GAINED_ENERGY.append(
                panel.getPanelEarningEnergy() * panel.getPanelNumber()) 
            if(energy_daily - bus_spended_energy > 0):
                if(battery_capacity < energy_daily - bus_spended_energy):
                    battery_balance += energy_daily - bus_spended_energy
                else:
                    battery_balance = battery_capacity
            else:
                print("Low Battery Daily")
                count += 1/24
        else:  # solar_panel_status = "off"
 
            if(not battery_balance-bus_spended_energy <= 0):
                battery_balance -= bus_spended_energy
                print()
                print("hours:",hoursIndex)
                print("Bus Spended::    ", bus_spended_energy)
                print("Battery Balance: ", battery_balance)
                print("Battert Capacity:", battery_capacity)
                print("Average balance: ", battery_balance - bus_spended_energy) 
                print()
                print()
            else:
                print("low battery")
                panel.increasePanelNum()
                count += 1/24
        energy_daily = 0
        DAILY_SPENDED_ENERGY.append(bus_spended_energy)
        bus_spended_energy = 0
    DAILY_DISTANCE.append(distance)
    DAILY_PASSANGER.append(passanger)
    distance = 0
    passanger = 0

    print(" ---------- Day:", daysIndex, " ---------- ")
    print("Daily Energy Balance:  ", TOTAL_GAINED_ENERGY, "Kw/h")
    print("Battery Balance:       ", battery_balance, "KW")

    print("")
    bus_spended_energy = 1
    energy_daily = 1
    if(random.choices(lossList, cum_weights=(1, 99))[0] == 1):
        TOTAL_LOSS_BUSS += 1
    if(random.choices(lossList, cum_weights=(1, 99))[0] == 1):
        TOTAL_LOSS_PANEL += 1

print()
print(count)
print()
print()
print()
print("Total Passed Days:     ", daysIndex, "days")
print("Total Panel Number:    ", panel.getPanelNumber(), "Peaces")
print("Total Bus Number:      ", oneBus.getTotalBusNum(), "Peaces")
print("Total Battery Number:  ", battery.getBatteryNum(), "Peaces")
print("Total Battery Capacity:", battery.getBatteryCapacity()
      * battery.getBatteryNum(), "KW")
print("Total Gained Energy:   ", TOTAL_GAINED_ENERGY, "Kw/h")
print("Total Spended Energy:  ", TOTAL_SPENDED_ENERGY, "Kw/h")
print("Balance:               ", TOTAL_GAINED_ENERGY - TOTAL_SPENDED_ENERGY, "Kw")
print("Total Passangers:      ", TOTAL_PASSANGER, "Person")
print("Total Lost Solar Panels", TOTAL_LOSS_PANEL, "Peaces")
print("Total Lost Busses      ", TOTAL_LOSS_BUSS, "Peaces")


print()
print("DAILY:")
dailyCount = 0
for i in DAILY_GAINED_ENERGY:
    dailyCount += i
print("Average Gained energy             ",
      dailyCount / len(DAILY_GAINED_ENERGY)*10 )
dailyCount = 0
for i in DAILY_SPENDED_ENERGY:
    dailyCount += i
print("Average Spended energy            ",
      dailyCount / len(DAILY_SPENDED_ENERGY)*24 )
dailyCount = 0
for i in DAILY_PASSANGER:
    dailyCount += i
print("Average Total Number of Passanger ", dailyCount / len(DAILY_PASSANGER))
dailyCount = 0
for i in DAILY_DISTANCE:
    dailyCount += i
print("Average Total Distance            ", dailyCount / len(DAILY_DISTANCE))

print()
print()
print()
 
