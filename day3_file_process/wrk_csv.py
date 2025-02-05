import csv
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["ename", "eid", "esal"])
    writer.writerow(["John", 1, 1000])
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
