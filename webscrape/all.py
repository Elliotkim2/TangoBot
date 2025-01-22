import scrape
import board
import solve
import mongodb

try:
    tango = board.filter(scrape.scrape())
    print(tango)
    data = tango.to_dict()
    mongodb.insert(data, "Boards")
    solvedGrid, moves = solve.solve(tango)
    data['moves'] = moves
    mongodb.insert(data, "SolvedBoards")
except Exception as e:
    print(f"Attempt failed: {e}")