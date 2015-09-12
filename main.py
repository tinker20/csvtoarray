import csv
with open('products.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['name'])
