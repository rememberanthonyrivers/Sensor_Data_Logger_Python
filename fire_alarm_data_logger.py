import csv, random, time 

def simulate_sensor():
    return random.uniform(50,105) # Simulated temperatures from 50 to 105°

csv_filename = "fire_alarm_data.csv"

while True:
    temperature = simulate_sensor()

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(csv_filename, mode='a', newline='') as csv_file:

        csv_writer = csv.writer(csv_file)

        csv_writer.writerow([str(timestamp)," - Temperature recorded : " + str(temperature)])

    print(f"Temperature: {temperature} °F")
    
    time.sleep(3)