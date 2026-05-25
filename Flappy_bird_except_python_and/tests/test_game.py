import unittest
from game import Game

class TestGame(unittest.TestCase):
    def test_init(self):
        game = Game()
        self.assertIsNotNone(game.screen)
        self.assertIsNotNone(game.clock)

if __name__ == "__main__":
    unittest.main()
```

[CMD]
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

[STATUS: SATISFIED] | [NEXT_STEP: Review and test the code]
https://github.com/user/Flappy_bird_except_python_and
