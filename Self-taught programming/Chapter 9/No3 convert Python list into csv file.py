import csv
list = [['Top Gun', 'Risky Business', 'Minority Report'],
        ['Titanic', 'The Revenant', 'Inception'],
        ['Training Day', 'Man on Fire', 'Flight']]
file = 'C:/Users/user/Desktop/Movies.csv'
with open(file, 'w') as f:
    w = csv.writer(f, delimiter = ',')
    for titles in list:
        w.writerow(titles)