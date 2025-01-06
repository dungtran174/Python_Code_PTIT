from datetime import datetime
class game:
    def __init__(self, id, name, start, end):
        self.name = name
        self.id = id
        self.khac = (datetime.strptime(end, '%H:%M')-datetime.strptime(start, '%H:%M')).seconds
    def __str__(self):
        return '{} {} {} gio {} phut'.format(self.id, self.name, self.khac//3600, self.khac%3600//60)
Game = [game(input(), input(), input(), input()) for i in range(int(input()))]
Game.sort(key=lambda x: x.khac, reverse=True)
print(*Game, sep='\n')