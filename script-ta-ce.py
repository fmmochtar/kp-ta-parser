import requests
import csv
from bs4 import BeautifulSoup

# Fetch the data from kp-ta ce undip (halaman TA)
page = requests.get('http://kp-ta.ce.undip.ac.id/index.php?/admin/pesertata/')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# write it into csv
f = csv.writer(open('daftar-ta-siskom.csv', 'w'))
f.writerow(['No', 'Nama / NIM', 'Judul / Tempat', 'Tgl mulai', 'Tgl seminar', 'Tgl sidang'])

# this is the table that we will try to dig its data
table_ta = soup.find('table',{'class':'table table-hover table-nomargin dataTable table-bordered'})

print ("Printing names listed in the table ...")

nodaftar = 1

for row in table_ta.select('tbody tr'):
    row_text = [x.text for x in row.find_all('td')]
    row_names = [x.text for x in row.find_all('a')]

    nama = ''.join(row_text[1])
    judul = ''.join(row_text[2])
    tglmulai = ''.join(row_text[3])
    tglseminar = ''.join(row_text[4])
    tglsidang = ''.join(row_text[5])

    f.writerow([nodaftar, nama, judul, tglmulai, tglseminar, tglsidang])

    nodaftar += 1

    print(nama)
