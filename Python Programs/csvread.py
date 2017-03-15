import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        date = row[0]
        color = row[3]

        dates.append(date)
        colors.append(color)

        
    print('The dates on record are: ', dates)
    
    
    while True:
        try:
            whatDate = input('What date do you wish to know the color of? ')
            dateIndex = dates.index(whatDate)
            theColor = colors[dateIndex]
            print('The color of', whatDate, 'is:', theColor)
            break
        except Exception:
            print('That date is not in the database.')
            
            

    
    

    
