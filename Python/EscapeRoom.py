oxygen_readings = [98, 95, 92, 60, 58, 95, 97, 90, 55, 99]
safe_level = 90
unsafe_readings = sum(1 for reading in oxygen_readings if reading < safe_level)
print(f"Unsafe Readings: {unsafe_readings}")
if unsafe_readings > 0:
    print("ALERT! There is an unsafe reading.")

pressure = 4 
external_door = "locked" 
security_key = False
timer = 8 
safe_pressure = 5 
while True:
    try:
        userpin = int(input("Please enter a pin: "))
        break
    except:
        print("Invalid PIN")
security_key = True if userpin == 2251 else False
if pressure < safe_pressure and external_door == "locked" and security_key == True and 0<=timer<=10:
    print(f"Airlock opened. Timer: {timer} minutes remaining.")
else:
    print(f"Warning: Cannot open airlock. Timer: {timer} minutes remaining.")

temperature_readings = []
while len(temperature_readings) < 12:
    try:
        usertemp = int(input("Please enter a temperature between 10 and 30: "))
        if usertemp<10 or usertemp>30:
            raise ValueError("Invalid temperature.")
        temperature_readings.append(usertemp)
    except:
        print("Invalid Temperature.")

out_of_range_count = sum(1 for reading in temperature_readings if not 18<=reading<=25)
print(f"Temps Out of Range {out_of_range_count}")
if out_of_range_count > 0:
    print("Warning: Some Temperatures are out of range.")
else:
    print("Room temperature is optimal.")
