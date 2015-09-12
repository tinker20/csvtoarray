import csv
with open('products(3).csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['name'])
