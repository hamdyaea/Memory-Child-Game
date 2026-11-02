# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
from collections import Counter
import unittest
from memory import MemoryGame, shuffled_cards

class MemoryTests(unittest.TestCase):
    def test_pairs(self):
        self.assertEqual(set(Counter(shuffled_cards()).values()), {2})
    def test_match(self):
        game = MemoryGame(cards=["Cat", "Dog", "Cat", "Dog"])
        self.assertEqual(game.select(0), "first")
        self.assertEqual(game.select(2), "match")
        self.assertEqual(game.matched, {0, 2})
        self.assertEqual(game.moves, 1)
    def test_mismatch(self):
        game = MemoryGame(cards=["Cat", "Dog", "Cat", "Dog"])
        game.select(0)
        self.assertEqual(game.select(1), "mismatch")
        self.assertEqual(game.select(2), "ignored")
        game.hide_unmatched()
        self.assertEqual(game.revealed, [])
    def test_win(self):
        game = MemoryGame(cards=["Cat", "Cat"])
        game.select(0)
        game.select(1)
        self.assertTrue(game.won)

if __name__ == "__main__":
    unittest.main()
