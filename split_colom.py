import pandas as pd

# Membaca file Excel
df = pd.read_excel('fix.xlsx')


# Membuat daftar unik dari nilai yang ingin Anda pisahkan
unique_values = df['PRODUCT_NAME'].unique()

# Iterasi melalui nilai unik dan menyimpan ke file .txt yang sesuai
for value in unique_values:
    # Memfilter dataframe berdasarkan nilai
    filtered_df = df[df['PRODUCT_NAME'] == value]
    
    # Mengambil kolom yang diinginkan dan menyimpannya ke file .txt
    filtered_df[['Script', 'Subscriber']].to_csv(f'{value}.txt', sep='\t', index=False)
