import pandas as pd

def fill_missing_values(file_path, output_path, fill_value="unknown"):
    # Đọc file CSV
    df = pd.read_csv(file_path)
    
    # Điền giá trị 'unknown' vào chỗ trống
    df.fillna(fill_value, inplace=True)
    
    # Lưu lại file mới
    df.to_csv(output_path, index=False)
    print(f"Dữ liệu đã được xử lý và lưu tại: {output_path}")

# Sử dụng hàm
file_path = "Watches.csv"
output_path = "Watches_cleaned.csv"
fill_missing_values(file_path, output_path)
