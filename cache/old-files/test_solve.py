import unittest
import subprocess
import solve
import mongodb
from board import TangoBoard

class TestClass (unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.boards = mongodb.get()
  
  def test_original(self):
    tango = TangoBoard([["E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "S", "M"], ["E", "E", "E", "E", "M", "S"], ["M", "S", "E", "E", "E", "E"], ["S", "M", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E"]],[[], [2, 7], [1, 8], [], [], [], [], [1, 8], [2, 7], [], [], [], [], [], [], [21], [], [], [], [], [21], [15, 20], [], [], [], [], [], [], [], [], [], [], [], [], [], []],[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [15, 20], [14], [], [], [], [], [14], [], [], [], [], [], [], [28, 33], [27, 34], [], [], [], [], [27, 34], [28, 33], []])

  def test_solve(self):
    for board in self.boards:
      g = board['grid']
      grid = []
      for s in g:
        grid.append(s[:])
      # grid = [g[0:6],g[6:12],g[12:18],g[18:24],g[24:30],g[30:36]]
      # print(grid)
      tango = TangoBoard(grid,board['crosses'], board['equals'], board['date'])
      solvedGrid, moves = solve.solve(tango)
      data = tango.to_dict()
      data['solvedGrid'] = solvedGrid
      data['moves'] = moves
      data['grid'] = board['grid']
      # print(board['grid'])
      mongodb.insert(data)