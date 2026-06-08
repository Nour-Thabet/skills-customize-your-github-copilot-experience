"""Starter code for the modular game assignment.

Fournit une structure minimale : Player, Enemy, Game.
Les étudiant·e·s doivent étendre et modulariser ce code en plusieurs fichiers/modules.
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Player:
    name: str
    score: int = 0

    def add_score(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.score += amount


@dataclass
class Enemy:
    kind: str
    hp: int = 1


class Game:
    def __init__(self) -> None:
        self.players: Dict[str, Player] = {}
        self.entities = []

    def add_player(self, player: Player) -> None:
        self.players[player.name] = player

    def remove_player(self, name: str) -> None:
        self.players.pop(name, None)

    def add_entity(self, entity) -> None:
        self.entities.append(entity)

    def step(self) -> None:
        """Advance a single tick of the game. For now, it awards 1 point to each player."""
        for p in self.players.values():
            p.add_score(1)


def demo() -> None:
    g = Game()
    g.add_player(Player("Alice"))
    g.add_player(Player("Bob"))
    g.add_entity(Enemy("slime", hp=2))
    print("Avant step:")
    for p in g.players.values():
        print(p.name, p.score)
    g.step()
    print("Après step:")
    for p in g.players.values():
        print(p.name, p.score)


if __name__ == "__main__":
    demo()
