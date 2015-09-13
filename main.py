import csv
with open('product(1).csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['_id'])
