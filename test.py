import pandas as pd
import difflib
import os

# 1. Membaca "Kamus" secara otomatis dari file CSV
file_kamus = 'kamus.csv'

# Mengecek apakah file ada agar program tidak error
if os.path.exists(file_kamus):
    # Pandas membaca file CSV secara otomatis
    df_kamus = pd.read_csv(file_kamus)
    
    # Pastikan data diubah ke huruf kecil semua dan menghapus spasi ekstra
    df_kamus['kata_baku'] = df_kamus['kata_baku'].str.lower().str.strip()
else:
    print(f"Error: File '{file_kamus}' tidak ditemukan!")
    # Membuat dataframe kosong sementara jika file tidak ada
    df_kamus = pd.DataFrame(columns=['kata_baku']) 

def auto_correct(kata_input, df):
    """
    Fungsi untuk mengecek dan mengoreksi kata yang typo.
    """
    if df.empty:
        return "Kamus kosong atau file tidak ditemukan."

    kata_input = kata_input.lower().strip()
    
    # Cek apakah kata sudah ada di kamus
    if kata_input in df['kata_baku'].values:
        return f"'{kata_input}' (Sudah Benar)"
    
    # Cari kata yang paling mirip
    daftar_kata = df['kata_baku'].tolist()
    koreksi = difflib.get_close_matches(kata_input, daftar_kata, n=1, cutoff=0.6)
    
    if koreksi:
        return f"Mungkin maksud Anda: '{koreksi[0]}'"
    else:
        return f"'{kata_input}' tidak dikenali."

# ==========================================
# Uji Coba Fungsi
# ==========================================
if not df_kamus.empty:
    print("--- Hasil Pengujian Auto-Correct ---")
    print(f"Input 'kmputer'  -> {auto_correct('kmputer', df_kamus)}")
    print(f"Input 'sekola'   -> {auto_correct('sekola', df_kamus)}")
    print(f"Input 'apel'     -> {auto_correct('apel', df_kamus)}")