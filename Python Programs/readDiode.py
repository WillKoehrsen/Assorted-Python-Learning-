import csv

diode_readings = {'diode1' : [], 'diode2': [], 'diode3': [], 'diode4': []}

with open('diode_readings.txt') as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		for diode in diode_readings:
			if len(row) != 0:
				for reading in row:
					diode_readings[diode].append(int(reading))

print(diode_readings.keys())

