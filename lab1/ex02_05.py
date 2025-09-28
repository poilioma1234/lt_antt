#nhập sô giờ làm
so_gio_lam = int(input("Nhập số giờ làm: "))
#nhập số tiền lương theo giờ
luong_gio = float(input("Nhập số tiền lương theo giờ: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
#tinh tong thu nhập
tong_thu_nhap = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"Tổng thu nhập: {tong_thu_nhap}")