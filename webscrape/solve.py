from board import TangoBoard
import board

'''
moves = [move]
move = [(x,y),<Sun/Moon>, Reason]

1.1: Cross
1.2: Equals

2.1.1: already 3 moons in row
2.1.2: already 3 moons in col
2.2.1: already 3 suns in row
2.2.2: already 3 suns in col

3.: neighbors already 2 in a row; e.g. E S S -> M S S or S E S -> S M S
  1: Vert. above (-12,-6,1)
  2: Vert. around (-6,6,2)
  3: Vert. below (6,12,3)
  4: Hor. before (-2,-1,4)
  5: Hor. around (-1,1,5)
  6: Hor. after (1,2,6)

4: if this is a _, row(.1)/col(.2) doesnt work
  isolates the row/column, find every possibility after filtering already locked and signs
  if spot n only has one option in every possibility, it must be that.

'''

def solve(board):
  # initialize helper variables to solve puzzle
  grid = []
  for cell in board.grid:
    grid.append(cell[:])
  # print(grid)
  crosses = board.crosses
  equals = board.equals
  sun_cols = [0]*6
  moon_cols = [0]*6
  sun_rows = [0]*6
  moon_rows = [0]*6

  moves = []
  possible_lines = ['SSMSMM', 'SSMMSM', 'SMSSMM', 'SMSMSM', 'SMSMMS', 'SMMSSM', 'SMMSMS', 'MSSMSM', 'MSSMMS', 'MSMSSM', 'MSMSMS', 'MSMMSS', 'MMSSMS', 'MMSMSS']
  # possible_lines = ['SSMSMM', 'SSMMSM', 'SMSSMM', 'SMSMSM', 'SMSMMS', 'SMMSSM', 'SMMSMS']

  def update_rows_cols(n):
    x,y = n % 6, n // 6
    if grid[n] == 'M':
      moon_cols[x]+=1
      moon_rows[y]+=1
    elif grid[n] == 'S':
      sun_cols[x]+=1
      sun_rows[y]+=1 

  def set_rows_cols():
    for n in range(36):
      update_rows_cols(n)
      
      
  def set_move(n,symbol,reason):
    grid[n] = symbol
    update_rows_cols(n)
    moves.append((n,symbol,reason))

  def valid(x,y):
    return 0 <= x < 6 and 0 <= y < 6

  def solve_cell(n):
  
    def check_1(n):
      def check_crosses(n):
        for neighbor in crosses[n]:
          neighbor = grid[neighbor]
          if neighbor != 'E':
            t = 'M' if neighbor == 'S' else 'S'
            set_move(n,t,"1.1")
            return True
        return False

      def check_equals(n):
        for neighbor in equals[n]:
          neighbor = grid[neighbor]
          if neighbor != 'E':
            set_move(n,neighbor,"1.2")
            return True
        return False
    
      return check_crosses(n) or check_equals(n)

    def check_2(n):
      x,y = n % 6, n // 6
      if moon_rows[y] >= 3:
        set_move(n,"S","2.1.1")
      elif moon_cols[x] >= 3:
        set_move(n,"S","2.1.2")
      elif sun_rows[y] >= 3:
        set_move(n,"M","2.2.1")
      elif sun_cols[x] >= 3:
        set_move(n,"M","2.2.2")
      else:
        return False
      return True
      
    def check_3(n):
      def check_3_helper(n,a,b):
        x,y = n % 6, n // 6
        ax,ay = x+a%6,y+a//6
        bx,by = x+b%6,y+b//6
        a = n + a
        b = n + b
        if not valid(ax,ay) or not valid(bx,by):
          return False
        if grid[a] != grid[b]:
          return False
        if grid[a] == 'E':
          return False
        return 'M' if grid[a] == 'S' else 'S'

      places_to_check = [(-12,-6,1),(-6,6,2),(6,12,3),(-2,-1,4),(-1,1,5),(1,2,6)]
      for a,b,c in places_to_check:
        t = check_3_helper(n,a,b)
        if t == 'M' or t == 'S':
          set_move(n,t,f'3.{c}')
          return True
      return False
      
    def check_4(n):
      def isolate_row():
        
        row = ''
        row_signs = ''
        y = n // 6
        for i in range(6):
          num = 6*y+i
          row+=grid[num]
          if num+1 in equals[num]:
            row_signs+='='
          elif num+1 in crosses[num]:
            row_signs+='x'
          else:
            row_signs+=' '
        return row, row_signs
      
      def isolate_col():
        col = ''
        col_signs = ''
        x = n % 6
        for i in range(6):
          num = 6*i+x
          col+=grid[num]
          if num+6 in equals[num]:
            col_signs+='='
          elif num+6 in crosses[num]:
            col_signs+='x'
          else:
            col_signs+=' '

        return col, col_signs
      
      def sign_filter(signs):
        
        filtered_ps= possible_lines
        for i, sign in enumerate(signs):
          ps = filtered_ps
          filtered_ps = []
          if sign == '=':
            filtered_ps = list(filter(lambda p: p[i] == p[i+1], ps))
          elif sign == 'x':
            filtered_ps = list(filter(lambda p: p[i] != p[i+1], ps))
          else:
            filtered_ps = ps
        return ps

      def current_filter(line, ps):
        def filter_line(s):
          for i in range(6):
            if line[i] == 'E':
              continue
            if line[i] != s[i]:
              return False
          return True
        filtered = list(filter(filter_line, ps))
        return filtered

      def check_same(ps,i):
        c = ps[0][i]
        for p in ps:
          if p[i] != c:
            return None
        return c

      def check_row():
        line, lines_signs = isolate_row()
        ps = sign_filter(lines_signs)
        ps = current_filter(line, ps)
        return check_same(ps, n % 6)

      def check_col():
        line, lines_signs = isolate_col()
        ps = sign_filter(lines_signs)
        ps = current_filter(line, ps)
        return check_same(ps, n // 6)

      t = check_row()
      if t:
        set_move(n,t,'4.1')
        return True
      t = check_col()
      if t:
        set_move(n,t,'4.2')
        return True
      return False

    if check_1(n):
      return True
    if check_2(n):
      return True
    if check_3(n):
      return True
    if check_4(n):
      return True
  
    
  set_rows_cols()
  n = 0
  while n < 36:
    if grid[n] == 'E':
      n = -1 if solve_cell(n) else n
    n += 1

  # print(grid)
  # print(moves)
  return grid, moves

# test 1
# tango = TangoBoard(["S", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],[[], [2, 7], [1, 8], [], [], [], [], [1, 8], [2, 7], [], [], [], [], [], [], [21], [], [], [], [], [21], [15, 20], [], [], [], [], [], [], [], [], [], [], [], [], [], []],[[1], [0], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []])
# # test 2
# tango = TangoBoard(["S", "S", "S", "E", "E", "E", "S", "S", "S", "E", "E", "E", "S", "S", "S", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],[[]]*36,[[]]*36)
# # test 3
# tango = TangoBoard(["S", "E", "S", "M", "M", "E", "E", "E", "E", "E", "E", "S", "S", "E", "E", "E", "E", "S", "S", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],[[]]*36,[[]]*36)
if __name__ =="__main__":
  tango = TangoBoard(["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "S", "M", "E", "E", "E", "E", "M", "S", "M", "S", "E", "E", "E", "E", "S", "M", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],[[], [2, 7], [1, 8], [], [], [], [], [1, 8], [2, 7], [], [], [], [], [], [], [21], [], [], [], [], [21], [15, 20], [], [], [], [], [], [], [], [], [], [], [], [], [], []],[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [15, 20], [14], [], [], [], [], [14], [], [], [], [], [], [], [28, 33], [27, 34], [], [], [], [], [27, 34], [28, 33], []])
  solve(tango)
  
    