import csv
with open('product.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['name'], row['price'])
