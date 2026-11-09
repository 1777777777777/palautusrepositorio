def sort_by_points(player):
    return player.points


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def nationality(self, nationality):
        players = []

        for player in self.players:
            if player.nationality == nationality:
                players.append(player)

        players.sort(key=sort_by_points, reverse=True)
        return players

    def team(self, team):
        players = []

        for player in self.players:
            if player.team == team:
                players.append(player)

        players.sort(key=sort_by_points, reverse=True)
        return players

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        players = list(self.players)

        # sort by goals (highest first) and return the requested slice
        players.sort(key=lambda p: p.goals, reverse=True)
        return players[:how_many]
