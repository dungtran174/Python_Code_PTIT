class Candidate:
    tong = 0

    def __init__(self, ten, ns, d1, d2, d3):
        self.ten = ten
        self.ns = ns
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.tong = d1 + d2 + d3

    def __str__(self):
        return f"{self.ten} {self.ns} {self.tong:.1f}"


print(Candidate(input(), input(), float(input()), float(input()), float(input())))
