#!/usr/bin/env python3
from ranking.utils import Retained


# noinspection PyUnresolvedReferences
class Match(Retained):
    def __init__(self, player_a, player_b, score: tuple):
        super().__init__()
        self.player_a = player_a
        self.player_b = player_b
        self.score = score
        if player_a > player_b:
            self._flip_order()

    def _flip_order(self):
        self.player_a, self.player_b = self.player_b, self.player_a
        self.score = (self.score[1], self.score[0])

    def __repr__(self):
        return f"<Match({self.player_a}, {self.player_b}, {self.score})>"


class Player(Retained):
    def __init__(self, identifier=None):
        super().__init__()
        self.identifier = self._generated_id if identifier is None else identifier

    def __repr__(self):
        return f"<Player(identifier={self.identifier}>"

    def __lt__(self, other):
        return self.identifier < other.identifier


class PlayerRating:
    def __init__(self, player):
        self.player = player

if __name__ == '__main__':
    pass
