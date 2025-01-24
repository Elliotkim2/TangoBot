import scrape
import board
import solve
import mongodb
import refresh
from datetime import datetime, timedelta

try:
    tango = board.filter(scrape.scrape())
    print(tango)
    data = tango.to_dict()
    mongodb.insert(data, "Boards")
    solvedGrid, moves = solve.solve(tango)
    data['moves'] = moves
    mongodb.insert(data, "SolvedBoards")

    date_15_days_ago = str((datetime.now() - timedelta(days=15)).date())
    mongodb.delete(date_15_days_ago)

    refresh.refresh()
except Exception as e:
    print(f"Attempt failed: {e}")
