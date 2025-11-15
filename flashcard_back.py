import pandas as pd
import os
import csv

def reorder_records(df, group_size=9, order_pattern=[3,2,1,6,5,4,9,8,7]):
    """Ubah urutan record sesuai pola tanpa kehilangan data"""
    new_rows = []
    for i in range(0, len(df), group_size):
        group = df.iloc[i:i+group_size]
        for j in order_pattern:
            if j <= len(group):
                new_rows.append(group.iloc[j-1])
    return pd.DataFrame(new_rows, columns=df.columns)

def read_csv_safe(file_path):
    """Baca CSV dengan deteksi otomatis delimiter dan encoding fallback"""
    encodings = ['utf-8', 'utf-8-sig', 'latin1', 'cp1252']
    last_error = None
    for enc in encodings:
        try:
            # Deteksi delimiter
            with open(file_path, 'r', encoding=enc, errors='ignore') as f:
                sample = f.read(4096)
                sniffer = csv.Sniffer()
                dialect = sniffer.sniff(sample)
                sep = dialect.delimiter
        except Exception:
            sep = ','

        try:
            df = pd.read_csv(file_path, sep=sep, dtype=str, keep_default_na=False,
                             encoding=enc, engine='python', on_bad_lines='skip')
            return df
        except Exception as e:
            last_error = e
            continue
    raise Exception(f"Gagal membaca CSV. Coba encoding lain. Detail: {last_error}")

def main():
    print("=== Flashcard CSV Reorder Tool (Versi Aman Semua Encoding) ===")
    while True:
        file_path = input("Masukkan nama file CSV (contoh: front.csv): ").strip('" ')
        if not os.path.isfile(file_path):
            print("❌ File tidak ditemukan. Pastikan nama dan lokasi file benar.")
            continue

        try:
            df = read_csv_safe(file_path)
        except Exception as e:
            print(f"❌ {e}")
            continue

        print(f"✅ File terbaca dengan {len(df)} record dan {len(df.columns)} kolom.")
        print(f"Kolom: {list(df.columns)}")

        try:
            result_df = reorder_records(df)
            output_path = os.path.splitext(file_path)[0] + "_reordered.csv"
            result_df.to_csv(output_path, index=False, encoding='utf-8-sig', quoting=csv.QUOTE_ALL)
            print(f"✅ Berhasil! File disimpan di: {output_path}")
            print(f"Jumlah record input: {len(df)}, output: {len(result_df)}")
        except Exception as e:
            print(f"❌ Gagal mengubah urutan record.\nError: {e}")
            continue

        again = input("Ingin konversi file lain? (y/n): ").strip().lower()
        if again != 'y':
            print("Selesai. Terima kasih sudah menggunakan Flashcard Reorder Tool!")
            break

if __name__ == "__main__":
    main()
