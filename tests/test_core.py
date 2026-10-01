import unittest

import core


class TestCore(unittest.TestCase):
    def test_00(self):
        state = core.new_game()
        state["items"] = [1]
        self.assertEqual(core.bug_6(state), 1)

    def test_01(self):
        state = core.new_game()
        core.bug_13(state)
        self.assertEqual(state["dst"], 5)

    def test_02(self):
        state = core.new_game()
        core.bug_20(state)
        self.assertNotIn(1, state["events"])

    def test_03(self):
        state = core.new_game()
        self.assertFalse(core.bug_27(state))

    def test_04(self):
        state = core.new_game()
        state["paused"] = True
        self.assertFalse(core.bug_4(state))

    def test_05(self):
        state = core.new_game()
        self.assertFalse(core.bug_11(state))
        self.assertEqual(state["balance"], 10)

    def test_06(self):
        state = core.new_game()
        self.assertTrue(core.bug_18(state))
        self.assertFalse(core.bug_18(state))

    def test_07(self):
        state = core.new_game()
        state["paused"] = True
        self.assertEqual(core.bug_25(state), 0)

    def test_08(self):
        state = core.new_game()
        self.assertIsNone(core.bug_2(state))

    def test_09(self):
        state = core.new_game()
        state["next_id"] = 7
        self.assertEqual(core.bug_9(state), 7)


if __name__ == "__main__":
    unittest.main()
