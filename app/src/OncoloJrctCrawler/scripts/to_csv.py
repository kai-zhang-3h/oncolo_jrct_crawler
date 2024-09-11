import json
import csv

data = []
with open('public/data.json') as f:
    for line in f:
        data.append(json.loads(line))

# encoding="utf_8_sig" to make sure csv file is properly output
with open('public/data.csv', 'w', newline='', encoding="utf_8_sig") as csvfile:
    fieldnames = list(data[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in data:
        writer.writerow(row)