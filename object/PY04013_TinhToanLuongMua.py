from datetime import datetime


class Data:
    def __init__(self, id, ten, bd, kt, luongmua):
        self.id = "T{:02d}".format(id)
        self.ten = ten
        self.time = datetime.strptime(kt, "%H:%M") - datetime.strptime(bd, "%H:%M")
        self.luongmua = luongmua

    def __str__(self):
        return "{:s} {:s} {:.2f}".format(
            self.id, self.ten, self.luongmua * 3600 / self.time.seconds
        )


list = []


def inList(data):
    for i in list:
        if i.ten == data.ten:
            i.luongmua += data.luongmua
            i.time += data.time
            return
    list.append(data)


for i in range(1, int(input()) + 1):
    data = Data(i, input(), input(), input(), int(input()))
    inList(data)


print(*list, sep="\n")
