#Hàm kiểm tra số nhị phân có chia hết cho 5 hay không
def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
#nhập chuỗi số nhị phân từ người dùng
so_nhi_phan = input("Nhập chuỗi số nhị phân (cách nhau bằng dấu phẩy): ")
#tach chuỗi các số nhị phân và kiểm tra chia hết cho 5
ds_so_nhi_phan = so_nhi_phan.split(',')
ket_qua = [so for so in ds_so_nhi_phan if chia_het_cho_5(so)]
#in ra kết quả
if len(ket_qua) > 0:
    print("Các số nhị phân chia hết cho 5 là: " + ','.join(ket_qua))
else:
    print("Không có số nhị phân nào chia hết cho 5.")