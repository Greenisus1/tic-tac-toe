import unittest,random,collections
import game
modules={'tic-tac-toe':game}
class Tests(unittest.TestCase):
 def test_tictac_win(self):self.assertEqual(modules['tic-tac-toe'].winner(list('XXXOO....')),'X')

 def test_tictac_illegal(self):
  m=modules['tic-tac-toe'];b=['.']*9;m.move(b,0,'X')
  with self.assertRaises(ValueError):m.move(b,0,'O')
 def test_tictac_draw(self):self.assertIsNone(modules['tic-tac-toe'].winner(list('XOXXOOOXX')))

if __name__=="__main__":unittest.main()
