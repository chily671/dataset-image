import csv

input_file = 'data.csv'
output_file = 'data_clean.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    rows = list(reader)  # Đọc tất cả dữ liệu vào list

    fixed_rows = []  # Danh sách chứa các dòng đã nối
    for i in range(0, len(rows), 2):  # Duyệt qua các dòng với bước nhảy 2 (để nối dòng i với dòng i+1)
        if i + 1 < len(rows):  # Kiểm tra xem dòng tiếp theo có tồn tại hay không
            row_1 = rows[i]  # Dòng chẵn (ví dụ: 2, 4, 6,...)
            row_2 = rows[i + 1]  # Dòng lẻ (ví dụ: 3, 5, 7,...)
            
            # Nối phần mô tả từ row_2 vào row_1
            row_1[1] += ' ' + row_2[1]  # Nối mô tả (giả sử mô tả nằm ở cột 2)
            
            # Thêm dòng đã nối vào danh sách
            fixed_rows.append(row_1)
        else:
            fixed_rows.append(rows[i])  # Nếu chỉ còn dòng chẵn, thêm nó vào như cũ

    writer.writerows(fixed_rows)  # Ghi các dòng đã sửa vào file mới
