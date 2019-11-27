import csv
import random
from Name import Name

root = ""
male_names_csv_path = root + "tr_isim_erkek.csv"
female_names_csv_path = root + "tr_isim_kadin.csv"

male_names = []
with open(male_names_csv_path, newline='', encoding='utf-8') as male_csv_file:
	reader = csv.DictReader(male_csv_file)
	for row in reader:
		male_names.append( Name(row['[isim]'], row['[sayi]']) )

female_names = []
with open(female_names_csv_path, newline='', encoding='utf-8') as female_csv_file:
	reader = csv.DictReader(female_csv_file)
	for row in reader:
		female_names.append( Name(row['[isim]'], row['[sayi]']) )


def names_starting_with(prefix, gender = "none"):
	names_to_use = []
	if gender is "male":
		names_to_use = male_names
	elif gender is "female":
		names_to_use = female_names
	else:
		names_to_use = male_names + female_names
	for name in names_to_use:
		print(name)

def rastgele_isim_al(gender = "none"):
	names_to_use = []
	if gender is "male":
		names_to_use = male_names
	elif gender is "female":
		names_to_use = female_names
	else:
		names_to_use = male_names + female_names
	rnd = random.choice(names_to_use)
	return rnd.get_name()

print(rastgele_isim_al())
print(rastgele_isim_al("male"))
print(rastgele_isim_al("female"))