import unittest

from player import Player
from statistics_service import StatisticsService, SortBy


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_matching_player(self):
        self.assertEqual(self.stats.search("Kurri").name, "Kurri")

    def test_search_returns_none_when_player_is_missing(self):
        self.assertIsNone(self.stats.search("Unknown"))

    def test_team_returns_only_matching_players(self):
        self.assertEqual(
            [player.name for player in self.stats.team("EDM")],
            ["Semenko", "Kurri", "Gretzky"],
        )

    def test_team_returns_empty_list_for_unknown_team(self):
        self.assertEqual(self.stats.team("UNKNOWN"), [])

    def test_top_returns_requested_number_in_points_order(self):
        self.assertEqual(
            [player.name for player in self.stats.top(3)],
            ["Gretzky", "Lemieux", "Yzerman"],
        )

    def test_top_with_zero_returns_no_players(self):
        self.assertEqual(self.stats.top(0), [])

    def test_top_with_more_than_available_returns_all_players(self):
        self.assertEqual(len(self.stats.top(10)), 5)
    def test_top_with_explicit_points(self):
        self.assertEqual(
            [p.name for p in self.stats.top(3, SortBy.POINTS)],
            ["Gretzky", "Lemieux", "Yzerman"],
        )

    def test_top_by_goals(self):
        self.assertEqual(
            [p.name for p in self.stats.top(3, SortBy.GOALS)],
            ["Lemieux", "Yzerman", "Kurri"],
        )

    def test_top_by_assists(self):
        self.assertEqual(
            [p.name for p in self.stats.top(3, SortBy.ASSISTS)],
            ["Gretzky", "Yzerman", "Lemieux"],
        )