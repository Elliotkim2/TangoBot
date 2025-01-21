import scrape
import board
import solve
import mongodb



for i in range(3):
    try:
        # Code that might raise an exception
        tango = board.filter(scrape.scrape())
        solvedGrid, moves = solve.solve(tango)
        data = tango.to_dict()
        data['moves'] = moves
        mongodb.insert(data)
        break  # Exit loop if successful
    except Exception as e:
        print(f"Attempt {i+1} failed: {e}")
else:
    print("All attempts failed.")