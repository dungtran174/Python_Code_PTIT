class NhanVien:
    def __init__(self, stt, ten, diem1, diem2):
        self.stt = "TS0" + str(stt)
        self.ten = ten
        self.diem1 = diem1
        self.diem2 = diem2
        while diem1 > 10:
            diem1 /= 10
        while diem2 > 10:
            diem2 /= 10
        self.diem = (diem1 + diem2) / 2
    def xl(self):
        if (self.diem <5):
            return "TRUOT"
        elif(self.diem < 8):
            return "CAN NHAC"
        elif(self.diem <= 9.5):
            return "DAT"
        else:
            return "XUAT SAC"
    def __str__(self):
        return self.stt + " " + self.ten + " " + "{:.2f}".format(self.diem) + " " + self.xl()

nhanvien = [NhanVien(t+1, input(), float(input()), float(input())) for t in range(int(input()))]
nhanvien.sort(key = lambda x: x.diem, reverse = True)
print(*nhanvien, sep = "\n")