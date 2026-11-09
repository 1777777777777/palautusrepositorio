import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player({
                "name": "Semenko",
                "nationality": "CAN",
                "team": "EDM",
                "goals": 4,
                "assists": 12,
            }),
            Player({
                "name": "Lemieux",
                "nationality": "CAN",
                "team": "PIT",
                "goals": 45,
                "assists": 54,
            }),
            Player({
                "name": "Kurri",
                "nationality": "FIN",
                "team": "EDM",
                "goals": 37,
                "assists": 53,
            }),
            Player({
                "name": "Yzerman",
                "nationality": "CAN",
                "team": "DET",
                "goals": 42,
                "assists": 56,
            }),
            Player({
                "name": "Gretzky",
                "nationality": "CAN",
                "team": "EDM",
                "goals": 35,
                "assists": 89,
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_nationality_returns_matching_players_in_points_order(self):
        players = self.stats.nationality("CAN")
        self.assertEqual(
            [p.name for p in players],
            ["Gretzky", "Lemieux", "Yzerman", "Semenko"],
        )

    def test_nationality_returns_empty_list_when_none_found(self):
        self.assertEqual(self.stats.nationality("SWE"), [])

    def test_team_returns_matching_players_in_points_order(self):
        players = self.stats.team("EDM")
        self.assertEqual(
            [p.name for p in players],
            ["Gretzky", "Kurri", "Semenko"],
        )

    def test_team_returns_empty_list_for_unknown_team(self):
        self.assertEqual(self.stats.team("DAL"), [])

    def test_top_goal_scorers_returns_requested_amount_in_goals_order(self):
        players = self.stats.top_goal_scorers(3)
        self.assertEqual(
            [p.name for p in players],
            ["Lemieux", "Yzerman", "Kurri"],
        )
