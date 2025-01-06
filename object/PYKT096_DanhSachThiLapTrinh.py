class Team:
    def __init__(self, id, ma, tenhd):
        self.id = 'Team{:02d}'.format(id)
        self.ma = ma
        self.tenhd = tenhd
class Ts:
    def __init__(self, id, ten, team):
        self.id = 'C{:03d}'.format(id)
        self.ten = ten
        self.team = team
    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.ten, self.team.ma, self.team.tenhd)
teams = [Team(i+1, input(), input()) for i in range(int(input()))]
ts = []
for i in range(int(input())):
    ten, team = input(), input()
    for j in teams:
        if j.id == team:
            ts.append(Ts(i+1, ten, j))
            break
print(*sorted(ts, key=lambda x: x.ten), sep='\n')