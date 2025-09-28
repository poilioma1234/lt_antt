#tạo 1 danh sách rỗng lưu kết quả
result = []
#duyệt qua hết tât cả các số trong đoạn từ 2000 đến 3200, kiểm tra xem số i có chia hết cho 7 và không phải bộ số của 5 không
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        result.append(str(i))
print(','.join(result))