import scrape
import board



for i in range(3):
    try:
        # Code that might raise an exception
        board.filter(scrape.scrape())
        break  # Exit loop if successful
    except Exception as e:
        print(f"Attempt {i+1} failed: {e}")
else:
    print("All attempts failed.")