import scrape
import board
import solve
import mongodb

tango = board.filter(scrape.scrape())
print(tango)
solvedGrid, moves = solve.solve(tango)
data = tango.to_dict()
data['moves'] = moves
mongodb.insert(data)

for i in range(3):
    try:
        # Code that might raise an exception
        tango = board.filter(scrape.scrape())
        print(tango)
        solvedGrid, moves = solve.solve(tango)
        data = tango.to_dict()
        data['moves'] = moves
        mongodb.insert(data)
        break  # Exit loop if successful
    except Exception as e:
        print(f"Attempt {i+1} failed: {e}")
else:
    print("All attempts failed.")