import csv
import random
from turkce_isimler.Name import Name

male_names_csv_path = "tr_isim_erkek_filtered.csv"
female_names_csv_path = "tr_isim_kadin_filtered.csv"
male_names = []
female_names = []

def setup():
	with open(male_names_csv_path, newline='', encoding='utf-8-sig') as male_csv_file:
		reader = csv.DictReader(male_csv_file)
		for row in reader:
			male_names.append( Name(row['isim'], row['sayi']) )

	with open(female_names_csv_path, newline='', encoding='utf-8-sig') as female_csv_file:
		reader = csv.DictReader(female_csv_file)
		for row in reader:
			female_names.append( Name(row['isim'], row['sayi']) )

def rastgele_isim_al(cinsiyet=None, sayi=1):
	"""Bu fonksiyon; erkek, kadın veya her iki cinsiyetten birden, bir veya daha fazla isim
	döndürür.
	
	Keyword Arguments:
		cinsiyet {string} -- erkek veya kadın (default: {None})
		sayi {int} -- Kaç tane isim döndürüleceği (default: {1})
	
	Raises:
		ValueError: Eğer cinsiyet geçersizse veya sayı 1'den küçükse hata verir.
	
	Returns:
		string ya da string listesi -- Eğer sayi 1 ise string döndürür, aksi takdirde
		string listesi döndürür.
	"""
	if len(male_names) == 0:
		setup()
	if not isinstance(sayi, int) or sayi < 1:
		raise ValueError("Sayı 0'dan büyük bir tam sayı olmalıdır")

	names_to_use = []
	if cinsiyet == "erkek":
		names_to_use = male_names
	elif cinsiyet == "kadın":
		names_to_use = female_names
	elif cinsiyet is None:
		names_to_use = male_names + female_names
	else:
		raise ValueError("Cinsiyet şunlardan biri olmalıdır: erkek, kadın")
	if len(names_to_use) < sayi:
		names_to_use = names_to_use * int((sayi / len(names_to_use) + 2))
	rnd = [x.get_name() for x in random.sample(names_to_use, sayi)]

	return rnd if len(rnd) != 1 else rnd[0]
