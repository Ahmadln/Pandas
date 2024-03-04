import pandas as pd

# Membaca file Excel
df = pd.read_excel('duplikat.xlsx')

# Menghapus duplikasi berdasarkan seluruh kolom
df = df.drop_duplicates()

# Menyimpan hasil ke file Excel baru
df.to_excel('nama_file_tanpa_duplikasi.xlsx', index=False)
