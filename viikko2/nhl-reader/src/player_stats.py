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
