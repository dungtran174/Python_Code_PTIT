a = []
class stu:
    def __init__(self, n, a, s) -> None:
        self.name = n
        self.ac = a
        self.submit = s
for i in range(int(input())):
    name = input()
    ac, submit = map(int, input().split())
    a.append(stu(name, ac, submit))
a.sort(key=lambda x: (-x.ac, x.submit, x.name))
for i in a: print(i.name, i.ac, i.submit)
        