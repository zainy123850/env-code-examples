def calculate_average(data):
    return sum(data) / len(data)

data = [72, 55, 101, 90]
average = calculate_average(data)
print("Average:", average)

stations = [["A1", 62], ["B2", 85], ["C3", 40], ["D4", 120]]
for station in stations:
    print(f"{station[0]} → {station[1]}")

def report_status(stations, threshold):
    for station in stations:
        name, pm25 = station
        status = "Safe" if pm25 <= threshold else "Unsafe"
        print(f"{name}: {pm25} → {status}")

report_status(stations, 100)
