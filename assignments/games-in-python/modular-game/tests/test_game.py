import importlib.util
from pathlib import Path


HERE = Path(__file__).parent.parent
MODULE_PATH = HERE / "starter-code.py"


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("starter_code", str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_player_add_score():
    mod = load_module(MODULE_PATH)
    Player = mod.Player
    p = Player("Test")
    assert p.score == 0
    p.add_score(5)
    assert p.score == 5


def test_game_step_awards_points():
    mod = load_module(MODULE_PATH)
    Game = mod.Game
    Player = mod.Player
    g = Game()
    g.add_player(Player("A"))
    g.add_player(Player("B"))
    # initial scores
    assert all(p.score == 0 for p in g.players.values())
    g.step()
    assert all(p.score == 1 for p in g.players.values())
