# TangoBot

install playwright

run 
```
python3 scrape.py > html.txt
python3 filter.py
```
output should be the board of the day.

sql.py is a template for inserting into the database
## table in database: Boards
| *id* |  *date*  |               *board*              |
|------|----------|------------------------------------|
|     1|2024-12-23|EEEEEEEMEEEESMSEMEESEMSSEEEEMEEEEEEE|
### Commands
```
SELECT * FROM boards; // displays entire table
SELECT * FROM boards WHERE date="?"; // queries for what u need
```

## TODOS
Perhaps find a better webscraper? works well once you get completely rendered HTML;

Develop logic for actually solving the game;

Finding a way to display all this info.
## AARON WANG
added crosses and equals array with the cell indexes associated can be translated to x and y cords if you want.
EX:
CROSSES [(3, 9), (8, 9), (8, 2), (20, 26), (25, 26), (25, 19), (26, 27), (26, 20), (26, 32)]
EQUALS [(9, 10), (9, 3), (9, 15)]
