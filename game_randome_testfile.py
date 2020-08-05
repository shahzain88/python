import unittest
import random_game_easyone as r_game_e_file


class TestMain(unittest.TestCase):
    def setUp(self):
        print("     \n((**\n  Tested ")

    def test_guess_pram1(self):
        '''the equle if statemant is '''
        result = r_game_e_file.guess_pram(1, 1)
        self.assertTrue(result)

    def test_guess_pram2(self):
        '''not equle if the statemant is '''
        result = r_game_e_file.guess_pram(1, 5)
        # (if user.. == rand...: )will return False if it was not true
        # because else will return the opsit bool of what the if statment will return
        self.assertFalse(result)

    def test_guess_pram3(self):
        '''outside of the expected value is '''
        result = r_game_e_file.guess_pram(-1000, 1)
        self.assertFalse(result)

    def test_guess_pram4(self):
        '''if the geiven value was string '''
        result = r_game_e_file.guess_pram(2, "2")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
