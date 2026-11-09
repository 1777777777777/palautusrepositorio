class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.nationality = data["nationality"]
        self.team = data["team"]
        self.goals = data["goals"]
        self.assists = data["assists"]
        self.points = self.goals + self.assists
